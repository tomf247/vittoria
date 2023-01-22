from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from products.models import Product
from . import models
class SignupForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class EditProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = "__all__"

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = models.Newsletter
        fields=['emails']
        

class AddProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = "__all__"