from django.urls import path
from . import views

app_name = 'products'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
]