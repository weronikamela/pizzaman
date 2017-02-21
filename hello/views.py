from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Product2


# Create your views here.
def index(request):
    return render(request, 'index.html', {'pizza_list': Product2.objects.all()})

def products(request):
    return render(request, 'products.html')

#def checkout(request):
#    return render(request, 'checkout.html')

def checkout(request, id):
    instance = get_object_or_404(Product, id=id)
    Context = {
        "name": instance.name,
        "instance": instance
    }
    return render(request, 'checkout.html', Context)