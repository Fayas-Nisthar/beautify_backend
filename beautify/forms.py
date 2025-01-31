from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

class ShopUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            ShopUser.objects.create(user=user)
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['contact', 'pic']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['type']

class ShopProfileForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=CategoryModel.objects.all(),
        widget=forms.CheckboxSelectMultiple, 
        required=True
    )
    class Meta:
        model = ShopProfileModel
        fields = ['name', 'contact', 'pic', 'location', 'preferredGender', 'category']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'shop', 'status']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'shop', 'rating']
