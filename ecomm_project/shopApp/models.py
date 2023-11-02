from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    category_desc = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering=('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shopApp:product_by_category', args=[self.slug])


    def __str__(self):
        return '{}'.format(self.category_name)

class Product(models.Model):
    prod_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    prod_desc = models.TextField(blank=True)
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prod_image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('prod_name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('shopApp:productDetail', args=[self.category.slug, self.slug])


    def __str__(self):
        return '{}'.format(self.prod_name)

