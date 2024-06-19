from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem, ShippingAddress
from .forms import ShippingForm
from cart.models import Cart
from django.contrib import messages
from products.models import Product
from cart.views import cart_view
from django.db import transaction

from cart.views import add_to_cart



def order_history(request):
    orders = Order.objects.filter(user=request.user)  # Adjust query as per your model relations
    return render(request, 'orders/order_history.html', {'orders': orders})




def confirm_order(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/confirm_order.html', {'order': order})



def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return render(request, 'orders/error.html', {'message': 'Your cart is empty.'})

    # Prepare cart view with error handling for non-existent products
    try:
        cart_view = {get_object_or_404(Product, id=int(pid)): qty for pid, qty in cart.items()}
    except ValueError:
        return render(request, 'orders/error.html', {'message': 'Invalid product data.'})

    if request.method == 'POST':

        # shipping_form = ShippingForm(request.POST)
        # if shipping_form.is_valid():

         with transaction.atomic():  # Ensures atomicity of the transaction
            order = Order.objects.create(user=request.user, total=0)
            total = 0

            for product, quantity in cart_view.items():
                if not product.available:  # Assuming there's an `is_available` field
                    messages.error(request, f'{product.name} is no longer available')
                    continue
                OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)
                total += product.price * quantity

            if total == 0:  # Check if total is zero or if no items were added
                messages.error(request, 'No available products to checkout')
                return redirect('orders:checkout')

            order.total = total
            order.save()

            # Clear the cart after checkout
            request.session['cart'] = {}
            messages.success(request, 'Your order has been placed successfully.')
            return redirect('orders:confirm', order_id=order.id)

    return render(request, 'orders/checkout.html', {'cart_items': cart_view})
