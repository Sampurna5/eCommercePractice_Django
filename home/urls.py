from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('category/<slug>', CategoryItemView.as_view(), name='category'),
    path('search', SearchView.as_view(), name='search'),
    path('account/signup', signup, name='signup'),
    path('account/login', login, name='login'),
    path('cart', CartView.as_view(), name='cart'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('delete-cart/<slug>', delete_cart, name='delete-cart'),
    path('add-single-item-cart/<slug>', add_single_item_cart, name='add-single-item-cart'),
    path('remove-single-item-cart/<slug>', remove_single_item_cart, name='remove-single-item-cart'),
]
