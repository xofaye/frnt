from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Listing, Profile, Location
from .models import get_image_path


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class SearchFurnitureForm(forms.Form):
    min_price = forms.IntegerField(min_value=0)
    max_price = forms.IntegerField(min_value=0)
    location = forms.CharField()


class EditProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)
    biography = forms.CharField(max_length=500, required=False)

    class Meta:
        model = Profile
        fields = ('profile_image', 'biography')


class LocationForm(forms.ModelForm):
    street_address = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=50, required=False)
    postal_code = forms.CharField(max_length=15, required=False)
    country = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Location
        fields = ('street_address', 'city', 'postal_code', 'country')
