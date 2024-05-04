from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name} | {self.price} | {self.description}'

# Create your models here.
