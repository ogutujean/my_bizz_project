from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from django.http import Http404
from products.models import Product

# def cart_view(request):
#     cart_items = Cart.objects.all()
#     return render(request, 'cart/cart.html', {'cart_items': cart_items})

# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     Cart.objects.create(user=request.user, product=product, quantity=1)
#     return redirect('cart:cart')


def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        cart_items.append({'product': product, 'quantity': quantity})

    # Make sure to return an HttpResponse object
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # product = Product.objects.get(id=product_id)
    # cart = cart_view(request)
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    # cart[product_id_str] = cart.get(product_id_str, 0) + 1
    request.session['cart'] = cart
    return redirect('cart:cart')










