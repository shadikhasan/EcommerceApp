from django.contrib import admin
from django.urls import path
from django.urls import path, include
from shop import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
]
