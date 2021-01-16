from . import views
from django.urls import path


urlpatterns = [
    path('fetch_products', views.fetch_products),
    path('get_product', views.get_product),
    path('get_product_sku', views.get_product_sku),
]