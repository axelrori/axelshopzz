from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)