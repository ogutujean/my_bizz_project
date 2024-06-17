from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
    path('history/', views.order_history, name='order_history'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirm/<int:order_id>/', views.confirm_order, name='confirm'),
]