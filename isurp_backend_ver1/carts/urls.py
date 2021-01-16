from . import views
from django.urls import path


urlpatterns = [
    path('get_cart', views.get_cart),
    path('remove_item', views.remove_item),
    path('change_qnt', views.change_qnt),
    path('add_to_cart', views.add_to_cart),
]