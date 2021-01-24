from . import views
from django.urls import path


urlpatterns = [
    path('getcustomer', views.get_customer),
    path('updateaddress', views.update_address),
    path('get_checkoutform', views.get_checkoutform),
    path('google_signin', views.google_signin),
    path('facebook_signin', views.facebook_signin),
]