from . import views
from django.urls import path


urlpatterns = [
    path('get-cart', views.get_cart),
    path('remove-item', views.remove_item),
    path('change-qnt', views.change_qnt),
    path('add-to-cart', views.add_to_cart),
]