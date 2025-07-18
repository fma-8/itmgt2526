from django.contrib import admin

from .models import Product
from .models import CartItem
from .models import Transaction
from .models import LineItem
from .models import PreorderSettings
from .models import ProductLimit

# Register your models here.

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(LineItem)
admin.site.register(PreorderSettings)
admin.site.register (ProductLimit)

@admin.register(Transaction) 
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'user', 
        'storename', 
        'created_at', 
        'pickup_date', 
        'pickup_time', 
        'payment_method', 
        'transaction_ref', 
        'items_summary',
    )
    
    list_filter = ('created_at', 'pickup_date', 'payment_method', 'storename')
    search_fields = ('user__username', 'transaction_ref', 'items_summary')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
