from django.contrib import admin

# Register the models in the admin site.
from .models import Pizza
from .models import Topping

admin.site.register(Pizza)
admin.site.register(Topping)