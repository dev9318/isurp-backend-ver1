from . import views
from django.urls import path


urlpatterns = [
    path('get_review', views.get_review),
    path('post_review', views.post_review),
]