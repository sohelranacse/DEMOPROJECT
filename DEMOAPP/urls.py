from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('test', views.test),
    path('sohel', views.test),
    path('brand', views.brand),
]