from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    pizza_list = [
        {
            'Name':'MARGHERITA',
            'Description':'Tomato Sauce, 100% Mozzarella Cheese and Oregano',
            'Price':'5$'},
        {
            'Name':'5 PEPPERS',
            'Description':'Garlic butter sauce, 100% Mozzarella Cheese, Oregano, beef and 5 Peppers',
            'Price':'6$'},
        {
            'Name':'NEW YORK HOT DOG',
            'Description':'Tomato sauce, 100% Mozzarella Cheese, Oregano, Sausage, Fried Onions and Mustard',
            'Price':'5$'},
        {
            'Name':'CHEESEHAM',
            'Description':'Tomato Sauce, !00% Mozzarella Cheese, Oregano, Ham and Extra Mozzarella Pasta Pan',
            'Price':'5$'},
        {
            'Name':'RUSTICA',
            'Description':'Tomato Sauce, 100% Mozzarella Cheese, Oregano, Pepperoni and Fresh Mushrooms',
            'Price':'5$'},
        {
            'Name':'VEGGIE LOVERS',
            'Description':'Tomato sauce, 100% Mozzarella Cheese, Oregano, Mix Vegetables, Sweet Corn, Tomato and Olives',
            'Price':'5$'}
    ]
    return render(request, 'index.html', {'pizza_list': pizza_list})


def products(request):
    return render(request, 'products.html')

