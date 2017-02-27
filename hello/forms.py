from django import forms
from django.core import validators
from django.core.validators import RegexValidator

class OrderForm(forms.Form):
    customerName = forms.CharField(
        max_length=255,
        label='Customer name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Name'
            }
        ),
        validators=[RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Name must be literal',
            code='invalid_name'
        )]
    )
    customerSurname = forms.CharField(
        max_length=255,
        label='Customer surname',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Surname'
            }
        ),
        validators=[RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Surname must be literal',
            code='invalid_surname'
        )]
    )
    customerStreet = forms.CharField(
        max_length=255,
        label='Street',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Street'
            }
        )
        ,
        validators=[RegexValidator(
            regex='^[a-zA-Z]*[0-9]*$|^[a-zA-Z]*[\s][0-9]*[a-zA-Z]*$',
            message='Street name must be literal',
            code='invalid_streetName'
        )]
    )
    customerPostalCode = forms.CharField(
        max_length=32,
        label='Postal code',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'PostalCode'
            }
        ),
        validators=[RegexValidator(
            regex='^[0-9]{2}\-[0-9]{3}$',
            message='Postal code invalid',
            code='invalid_postalcode'
        )]
    )
    customerCity = forms.CharField(
        max_length=80,
        label='Customer city',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'City'
            }
        ),
        validators=[RegexValidator(
            regex='^[a-zA-Z]*$',
            message='City name must be literal',
            code='invalid_city'
        )]
    )
    customerEmail = forms.EmailField(
        max_length=80,
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Email'
            }
        ),
        validators=[validators.EmailValidator],
    )
    customerPhone = forms.CharField(
        max_length=40,
        label='Phone',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-button-medium',
                'placeholder': 'Phone'
            }
        )
        ,
        validators=[RegexValidator(
            regex='^[0-9]{9}$|^(\d{3}[\s]\d{3}[\s]\d{3})$|^(\d{3}[\-]\d{3}[\-]\d{3})$',
            message='Invalid number',
            code='Invalid_number'
        )]
    )
