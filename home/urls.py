from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('category/<slug>', CategoryItemView.as_view(), name='category'),
    path('search', SearchView.as_view(), name='search'),
    path('account', signup, name='signup'),
    path('login', login, name='login'),
]
