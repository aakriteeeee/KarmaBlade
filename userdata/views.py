from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def registration_success(request):
    return render(request, 'registration_success.html')