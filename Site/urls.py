from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('<int:pk>/hotel_detail/', views.hotel_details, name='hotel-detail'),
    path('count/<int:pk>/', views.count, name='count'),
    path('book/', views.booking_view, name='booking')
]