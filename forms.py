# core/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Pet
from .models import CareGiver


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'breed', 'description', 'photo', 'location']


class CareGiverForm(forms.ModelForm):
    class Meta:
        model = CareGiver
        fields = ['full_name', 'email', 'phone_number', 'bio', 'photo', 'location']
