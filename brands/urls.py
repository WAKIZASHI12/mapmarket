# brands/urls.py
from django.urls import path
from .views import brand_location, brand_search

urlpatterns = [
    path('brand/location/', brand_location, name='brand_location'),
    path('brand/search/', brand_search, name='brand_search'),
]