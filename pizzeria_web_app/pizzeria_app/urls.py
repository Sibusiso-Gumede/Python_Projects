"""Defines URL patterns for the Pizzeria App"""

from django.urls import path
from . import views

# For disambiguity purposes.
app_name = 'pizzeria_app'

urlpatterns = [
    # The homepage for the web app.
    path('', views.index, name='index'),
    # The list of all the pizzas.
    path('pizzas/', views.pizzas, name='pizzas'),
    # This lists all the pizzas and their toppings.
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
]