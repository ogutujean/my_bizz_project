from django.shortcuts import render
from .models import Product, Category
from django.db.models import Q



def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.filter(available=True)
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'products/product_list.html', {'products': products})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


