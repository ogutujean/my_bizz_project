from django.shortcuts import render, redirect
from .models import Order, OrderItem, ShippingAddress
from .forms import ShippingForm
from cart.models import Cart
from django.contrib import messages
from products.models import Product
from cart.views import cart_view

from cart.views import add_to_cart


def order_history(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_history.html', {'orders': orders})



# def checkout(request):
#     cart_items = Cart.objects.filter(user=request.user)

#     if not cart_items.exists():
#         return render(request, 'orders/error.html', {'message': 'Your cart is empty.'})

#     if request.method == 'POST':
#         with transaction.atomic():

#             order = Order.objects.create(user=request.user, total=0)
#             total = 0

#             for item in cart_items:
#                 if not item.product_id:

#                     print(f"Error: Product ID missing for cart item {item.id}")
#                     continue

#                 OrderItem.objects.create(
#                         order=order,
#                         product=item.product,
#                         quantity=item.quantity,
#                         price=item.product.price
#                 )
#                 total += item.product.price * item.quantity

#         order.total = total
#         order.save()

#         cart_items.delete()  # Optionally clear the cart after successful checkout
#         return redirect('order:confirm')  # Redirect to a confirmation page
    
#     return render(request, 'orders/checkout.html', {'cart_items': cart_items})


# def confirm_order(request, order_id):
#     order = Order.objects.get(id=order_id)
#     # product= product.objects.get()
#     return render(request, 'orders/confirm_order.html', {'order': order})


# def checkout(request):

#     cart = request.session.get('cart', {})
#     if not cart:
#         return render(request, 'orders/error.html', {'message': 'Your cart is empty.'})
#     try:
#         cart_details = {Product.objects.get(id=int(pid)): qty for pid, qty in cart.items()}
#     except ValueError:
#     # Handle the case where pid is not convertible to int
#         return render(request, 'orders/error.html', {'message': 'Invalid product data.'})

#     if request.method == 'POST':
#         product_id = Product.objects.get(str(id=id))
#         order = Order.objects.create(user=request.user if request.user.is_authenticated else None, total=0)
#         for product_id, quantity in cart.items():
#             product = Product.objects.get(id=product_id)
#             OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)
#         request.session['cart'] = {}  # Clear the cart after checkout
#         return redirect('order:confirm')

#     cart_details = {Product.objects.get(id=pid): qty for pid, qty in cart.items()}
#     return render(request, 'orders/checkout.html', {'cart_items': cart_details.items()})




def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return render(request, 'orders/error.html', {'message': 'Your cart is empty.'})

    try:
        cart_details = {Product.objects.get(id=int(pid)): qty for pid, qty in cart.items()}
    except ValueError:
        # Handle the case where pid is not convertible to int
        return render(request, 'orders/error.html', {'message': 'Invalid product data.'})

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total=0)
        total = 0
        for pid, quantity in cart.items():
            product = Product.objects.get(id=pid)
            order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)
            total += product.price * quantity
        
        # Update the total price of the order
        order.total = total
        order.save()
        
        # Clear the cart after checkout
        request.session['cart'] = {}
        return redirect('order_history')

    return render(request, 'orders/checkout.html', {'cart_items': cart_details.items()})



def confirm_order(request):
    return render(request, 'orders/confirm_order.html')