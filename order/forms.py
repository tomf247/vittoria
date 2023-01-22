from django import forms
from .models import Order

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
class CheckoutForm(forms.ModelForm):
    country =CountryField(blank_label='(select country)').formfield(
     required=False,
     widget=CountrySelectWidget(attrs={
         'class': 'custom-select d-block w-100',
     }))
    class Meta:
        model = Order
        fields = ('name','email','country','phone','street_name','apartment_name','city_name','postal_code')