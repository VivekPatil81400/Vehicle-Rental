import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Customers
from .forms import CustomerForm 
from django.contrib.auth.decorators import login_required  


# Create your views here.
@login_required
def add_customer(request):
    form = CustomerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'customer-form.html', {'form':form})



def customer_list(request):
    customers = Customers.objects.all()
    context = {
        'customers':customers
    }   
    return render(request,'customer_list.html',context)




