from django.shortcuts import render
from .models import Pizza

def index(request):
    """The homepage for pizzeria."""
    return render(request, 'pizzeria_app/index.html')

def pizzas(request):
    """This shows all pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria_app/pizzas.html', context)

def pizza(request, pizza_id):
    """This shows a detailed description of a pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeria_app/pizza.html', context)