from django.db import models

# Create your models here.

class Product(models.Model):
    upc= models.CharField(max_length=32, unique=True, db_index=True)
    name= models.CharField(max_length=200)
    price= models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(Self):
        return f"{self.upc} - {self.name} (${self.price})"