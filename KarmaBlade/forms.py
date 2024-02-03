# userdata/forms.py
from django import forms
from userdata.models import UserData

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['user_name', 'user_phone', 'user_email', 'user_password', 'user_cpassword']
