from django import forms
from django.core import validators

class OrderForm(forms.Form):
    customerName = forms.CharField(
        max_length=32,
        label ="Customer's name",
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Name'
            }
        )
    )
    customerSurname = forms.CharField(
        max_length=32,
        label ="Customer's surname",
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Surname'
            }
        )
    )
    customerStreet = forms.CharField(
        max_length=32,
        label ="Customer's street and number address",
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Street'
            }
        )
    )
    customerPostalCode = forms.CharField(
        max_length=32,
        label ="Customer's postal code",
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'PostalCode'
            }
        )
    )
    customerCity = forms.CharField(
        max_length=32,
        label ="Customer's city",
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'City'
            }
        )
    )
    customerEmail = forms.EmailField(
        max_length=32,
        label ="Customer's email",
        validators=[validators.validate_email],
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Email'
            }
        )
    )
    customerPhone = forms.CharField(
        max_length=32,
        label ="Customer's phone number",
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Phone'
            }
        )
    )
