from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class PreorderSettings(models.Model): #admin days pre-order limiter
    max_days_in_advance = models.PositiveIntegerField(default=7)
    def __str__(self):
        return f"Preorders allowed up to {self.max_days_in_advance} days in advance"

class Product(models.Model): #product list
    pic = models.URLField(blank = True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    desc = models.CharField(max_length=150)
    allergy = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
    
class ProductLimit(models.Model): #admin product allocation pre-order limiter
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    daily_limit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - Limit: {self.daily_limit}"

class CartItem(models.Model): #cart items
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField()
    refno = models.IntegerField(default=123455677)
    
    @property
    def totalprice(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f'{self.quantity} of {self.product} (User: {self.user.username}) @ PHP {self.totalprice}'
    
class Transaction(models.Model): #final transactions to be displayed on history
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField()
    storename = models.CharField(default='Resto1')
    
    payment_method = models.CharField(
        max_length=20,
        choices=[('cash', 'Cash'), ('online', 'Online')],
        null=True,
        blank=True
    )
    pickup_date = models.DateField(null=True, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)
    transaction_ref = models.CharField(max_length=100, null=True, blank=True)  # gcash reference

    items_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Transaction on {self.created_at} by {self.user.username}. GCash Reference: {self.transaction_ref}. Order Number {self.id}'


class LineItem(models.Model): #lineitems 
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField()
    storename = models.CharField(default="Sip 'n' Scoop") #change according to actual name
    
    @property
    def subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f'{self.transaction, self.product, self.quantity, self.storename}'