from . import views
from django.urls import path


urlpatterns = [
    path('verify_order', views.verify_order),
    path('return_order', views.return_order),
]