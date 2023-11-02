from django.db import models
from shopApp.models import Category, Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True, unique=True)
    date_added = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return str(self.cart_id)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.prod_price * self.quantity

    def __str__(self):
        return str(self.product)