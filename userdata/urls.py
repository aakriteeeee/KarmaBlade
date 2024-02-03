from django.urls import path

from KarmaBlade.views import register, registration_success

urlpatterns = [
    path('register/', register, name='register'),
    path('registration_success/', registration_success, name='registration_success'),
    
]



