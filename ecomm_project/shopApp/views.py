from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def index(request):
    return HttpResponse("Hello")

def AllProductCat(request, c_slug=None,):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page, availability=True)
    else:
        products_list = Product.objects.all().filter(availability=True)

    # pagination
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    #     pagination ends

    return render(request, 'category.html', {'category':c_page, 'products':products})

def prod_detail(request, p_slug, c_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product':product})