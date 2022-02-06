from django.shortcuts import render, redirect
from .forms import Rentalform
from .models import Booking, Vehicles

# Create your views here.

def rental_booking(request):
    form = Rentalform(request.POST or None)  

    obj1 = Vehicles.objects.get(id=1)
    bike_count = obj1.count

    obj2 = Vehicles.objects.get(id=2)
    cycle_count = obj2.count

    obj3 = Vehicles.objects.get(id=3)
    car_count = obj3.count

    obj4 = Vehicles.objects.get(id=4)
    boat_count = obj4.count

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'rental-form.html', {'form':form})

def rental_list(request):
    bookings = Booking.objects.all()
    context = {
        'bookings':bookings
    }   
    return render(request,'rental_list.html',context)


#inventory
