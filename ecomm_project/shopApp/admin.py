from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name', 'prod_price', 'stock', 'availability', 'created', 'updated', 'prod_image']
    list_editable = ['prod_price', 'stock', 'availability']
    prepopulated_fields = {'slug':('prod_name',)}
    list_per_page = 20
admin.site.register(Product, ProductAdmin)
