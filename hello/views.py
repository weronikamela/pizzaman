from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Product


# Create your views here.
def index(request):
    return render(request, 'index.html', {'pizza_list': Product.objects.all()})

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


def initialize_database(request):
    Product.objects.all().delete()
    p = Product(
        name='MARGHERITA',
        description='Tomato Sauce, 100% Mozzarella Cheese and Oregano',
        price=5,
        currency='USD',
        picture='http://flyingforkcafe.com/wp-content/uploads/2016/06/porcini-pizza-400x250.jpg')
    p.save()
    p = Product(
        name='5 PEPPERS',
        description='Garlic butter sauce, 100% Mozzarella Cheese, Oregano, beef and 5 Peppers',
        price=5,
        currency='USD',
        picture='http://flyingforkcafe.com/wp-content/uploads/2016/06/porcini-pizza-400x250.jpg')
    p.save()
    p = Product(
        name='NEW YORK HOT DOG',
        description='Tomato sauce, 100% Mozzarella Cheese, Oregano, Sausage, Fried Onions and Mustard',
        price=5,
        currency='USD',
        picture='http://flyingforkcafe.com/wp-content/uploads/2016/06/porcini-pizza-400x250.jpg')
    p.save()
    p = Product(
        name='CHEESEHAM',
        description='Tomato Sauce, !00% Mozzarella Cheese, Oregano, Ham and Extra Mozzarella Pasta Pan',
        price=5,
        currency='USD',
        picture='http://flyingforkcafe.com/wp-content/uploads/2016/06/porcini-pizza-400x250.jpg')
    p.save()
    p = Product(
        name='RUSTICA',
        description='Tomato Sauce, 100% Mozzarella Cheese, Oregano, Pepperoni and Fresh Mushrooms',
        price=5,
        currency='USD',
        picture='http://flyingforkcafe.com/wp-content/uploads/2016/06/porcini-pizza-400x250.jpg')
    p.save()
    p = Product(
        name='VEGGIE LOVERS',
        description='Tomato sauce, 100% Mozzarella Cheese, Oregano, Mix Vegetables, Sweet Corn, Tomato and Olives',
        price=5,
        currency='USD',
        picture='http://flyingforkcafe.com/wp-content/uploads/2016/06/porcini-pizza-400x250.jpg')
    p.save()

    return redirect('/')

