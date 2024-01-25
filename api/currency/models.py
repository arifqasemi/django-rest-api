from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Currency(models.Model):
    base = models.CharField(max_length=255)
    counter = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=5)