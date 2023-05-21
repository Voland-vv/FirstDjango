from django.db import models

class Color(models.Model):
   name = models.CharField(max_length=32)
   css_view = models.CharField(max_length=32, default='none')


class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   description = models.TextField(max_length=5000, default='Описание товара')
   colors = models.ManyToManyField(to=Color)

   def __repr__(self):
      return f'Item: {self.name} | {self.brand}'
