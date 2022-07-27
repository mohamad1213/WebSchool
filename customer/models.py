from django.db import models

class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

