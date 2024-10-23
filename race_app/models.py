from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)

    def _str__(self):
        return self.brand