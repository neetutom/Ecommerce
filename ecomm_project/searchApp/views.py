from django.shortcuts import render
from shopApp.models import Product
from django.db.models import Q


# Create your views here.
def searchResult(request):
    print(request)
    products = None
    query = None
    if 'search' in request.GET:
        query = request.GET.get('search')
        products = Product.objects.all().filter(Q(prod_name__contains=query) | Q(prod_desc__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})
