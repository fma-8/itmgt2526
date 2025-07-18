from django.http import HttpResponse
from django.template import loader
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import (
    login, logout, authenticate
)
from django.contrib import messages
from .models import CartItem
from .models import Transaction
from .models import LineItem
from .models import PreorderSettings
from .models import ProductLimit
import datetime as dt
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime, timedelta, date
from django.utils.timezone import now

@login_required
def mainpage(request):
    template = loader.get_template("resto1/mainpage.html")
    today = now().date()

    pickup_date_str = request.GET.get('pickup_date')  
    if pickup_date_str:
        try:
            pickup_date = datetime.strptime(pickup_date_str, '%Y-%m-%d').date()
        except ValueError:
            pickup_date = today
    else:
        pickup_date = today

    preorder_settings = PreorderSettings.objects.first()
    max_days = preorder_settings.max_days_in_advance if preorder_settings else 7

    if pickup_date > today + timedelta(days=max_days):
        pickup_date = today + timedelta(days=max_days)

    products = Product.objects.all()
    product_limits = {}

    for product in products:
        limit_obj = ProductLimit.objects.filter(product=product).first()
        limit = limit_obj.daily_limit if limit_obj else None

        sold_qty = LineItem.objects.filter(
            product=product,
            transaction__pickup_date=pickup_date
        ).aggregate(total=Sum('quantity'))['total'] or 0

        remaining = max(0, (limit - sold_qty)) if limit is not None else 999
        product_limits[product.id] = remaining

    context = {
        'productlist': products,
        'pickup_date': pickup_date,
        'today': today,
        'max_days': max_days,
        'product_limits': product_limits,
    }

    return HttpResponse(template.render(context, request))

    

@login_required
def checkout(request):
    if request.method == 'POST':
        if 'payment_method' in request.POST:
            payment_method = request.POST.get("payment_method")
            pickup_date_str = request.POST.get("pickup_date")
            try:
                pickup_date = dt.datetime.strptime(pickup_date_str, "%Y-%m-%d").date()
            except (ValueError, TypeError):
                pickup_date = now().date()

            pickup_time = (
                dt.datetime.strptime(request.POST.get("pickup_time"), "%H:%M").time()
                if payment_method == "online" and request.POST.get("pickup_time")
                else None
            )

            transaction_ref = request.POST.get("transaction_ref") if payment_method == "online" else None

            transaction = Transaction.objects.create(
                user=request.user,
                created_at=timezone.now(),
                payment_method=payment_method,
                pickup_date=pickup_date,
                pickup_time=pickup_time,
                transaction_ref=transaction_ref,
                items_summary=""
            )

            cart_items = CartItem.objects.filter(user=request.user)
            summary_parts = []

            for item in cart_items:
                LineItem.objects.create(
                    transaction=transaction,
                    product=item.product,
                    quantity=item.quantity,
                )
                summary_parts.append(f"{item.quantity}x {item.product.name}")
                item.delete()

            transaction.items_summary = ', '.join(summary_parts)
            transaction.save()

            request.session['last_transaction_id'] = transaction.id
            return redirect('confirmation')

        else:

            CartItem.objects.filter(user=request.user).delete()

            products = Product.objects.all()
            for product in products:
                qty = int(request.POST.get(f'quantity_{product.id}', 0))
                if qty > 0:
                    CartItem.objects.create(
                        user=request.user,
                        product=product,
                        quantity=qty
                    )

            pickup_date = request.POST.get("pickup_date")
            request.session['pickup_date'] = pickup_date 
            return redirect('checkout') 

    else:
        template = loader.get_template("resto1/checkout.html")
        cart_items = CartItem.objects.filter(user=request.user)
        grand_total = sum(item.totalprice for item in cart_items)

        pickup_date_str = request.session.get("pickup_date")
        try:
            pickup_date = dt.datetime.strptime(pickup_date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            pickup_date = now().date()

        context = {
            'cart_items': cart_items,
            'grand_total': grand_total,
            'pickup_date': pickup_date
        }
    return HttpResponse(template.render(context, request))


@login_required
def confirmation(request):
    transaction_id = request.session.get('last_transaction_id')
    if not transaction_id:
        return redirect('mainpage')

    transaction = Transaction.objects.filter(id=transaction_id, user=request.user).first()
    if not transaction:
        return redirect('mainpage')

    items = LineItem.objects.filter(transaction=transaction)
    grand_total = sum(item.product.price * item.quantity for item in items)

    context = {
        "transaction": transaction,
        "items": items,
        "grand_total": grand_total
    }

    template = loader.get_template("resto1/confirmation.html")
    return HttpResponse(template.render(context, request))

@login_required
def transactions_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
    template = loader.get_template("resto1/transactions.html")
    context = {
        "transactions": transactions
    }
    return HttpResponse(template.render(context, request))