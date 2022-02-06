from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.customer_list, name='customer_list'),
    path('add', views.add_customer, name='add_customer'),
]