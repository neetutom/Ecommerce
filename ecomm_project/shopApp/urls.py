from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shopApp import views

app_name = 'shopApp'

urlpatterns = [
    path('', views.AllProductCat, name='allProductCat'),
    path('<slug:c_slug>/', views.AllProductCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:p_slug>', views.prod_detail, name='productDetail'),
]
