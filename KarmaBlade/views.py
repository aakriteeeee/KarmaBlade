from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from shop.models import Product
from userdata.models import UserData
from KarmaBlade.forms import RegistrationForm




import sys
sys.path.append('d:\\Django\\KarmaBlade\\KarmaBlade') 

print(5)


def homepage(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def shop(request):
    ProductData=Product.objects.all()
    data={
        'ProductData': ProductData
    }
    return render(request,'shop.html', data)
def cart(request):
    return render(request,'cart.html')
def contact(request):
    return render(request,'contact.html')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

    
def login(request):
    return render(request,'login.html')
def registration_success(request):
    return render(request, 'registration_success.html')
