from django import forms

class OrderForm(forms.Form):
    # productId           = forms.IntegerField()
    customerName        = forms.CharField(max_length=32)
    customerSurname     = forms.CharField(max_length=32)
    customerStreet      = forms.CharField(max_length=32)
    customerPostalCode  = forms.CharField(max_length=32)
    customerCity        = forms.CharField(max_length=32)
    customerEmail       = forms.CharField(max_length=32)
    # customerPhone       = forms.CharField(max_length=10)