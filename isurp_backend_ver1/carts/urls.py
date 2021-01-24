from . import views
from django.urls import path


urlpatterns = [
    path('getcart', views.get_cart),
    path('removeitem', views.remove_item),
    path('changeqnt', views.change_qnt),
    path('addtocart', views.add_to_cart),
    path('clear', views.clear_cart),
]