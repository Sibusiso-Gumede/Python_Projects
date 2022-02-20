from django.db import models

class Pizza(models.Model):
    """A description of a specific type of pizza."""
    # A field to hold name values.
    name = models.CharField(max_length=50)
    # A field to track the date which the pizza entry was created.
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.name

class Topping(models.Model):
    """The ingredients added to the pizza."""
    # A field that represents an association with the pizza model.
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    # The on_delete=models.CASACADE argument tells django to delete
    # all the Toppings assocated with a Pizza model when it's deleted.
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.name