from . import views
from django.urls import path

urlpatterns = [
    path('booking', views.rental_booking, name='booking'),
    path('rental-list', views.rental_list, name='rental_list')
]