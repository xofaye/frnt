from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Listing, Profile, Location, ListingPicture
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
    query = forms.CharField(initial="", required=True)
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)
    location = forms.CharField(max_length=100, required=False)


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


class ListingPictureForm(forms.ModelForm):
    url = forms.CharField(max_length=500, required=True)

    class Meta:
        model = ListingPicture
        fields = ('url',)


class AddListingForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500, required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Listing
        fields = ('title', 'description', 'price')


class EditListingForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500, required=False)
    picture = forms.ImageField(required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Listing
        fields = ('title', 'description', 'picture', 'price')