from django.urls import path
from . import views

app_name = 'products'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),   #added
]