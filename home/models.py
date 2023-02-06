from django.db import models
from django.utils.timezone import now

# Create your models here.

EXPENSE_CATEGORIES = [
    ("Food", "Food"),
    ("Travel", "Travel"),
    ("Shopping", "Shopping"),
    ("Necessities", "Necessities"),
    ("Entertainment", "Entertainment"),
    ("Subscriptions", "Subscriptions"), 
    ("Other", "Other")
]

INCOME_CATEGORIES = [
    ("Work", "Work"),
    ("Other", "Other")
]


class Expense(models.Model):
    name = models.CharField(max_length = 25)
    category = models.CharField( max_length = 25, choices = EXPENSE_CATEGORIES, default = 'Food')
    amount = models.DecimalField(max_digits = 7,decimal_places = 2, default = 0)
    date = models.DateField(default = now)

    def __str__(self):
        return self.name

class Income(models.Model):
    name = models.CharField(max_length = 25)
    category = models.CharField(max_length = 25, choices = INCOME_CATEGORIES, default = 'Work')
    amount = models.DecimalField(max_digits = 7, decimal_places = 2, default = 0)
    date = models.DateField(default = now)

    def __str__(self):
        return self.name