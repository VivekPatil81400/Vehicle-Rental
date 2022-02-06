from. import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', include('customers.urls')),
    path('rental', include('vehicles.urls')),
]