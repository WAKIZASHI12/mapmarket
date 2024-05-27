
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    coordinates = models.CharField(max_length=100)  
    directions = models.TextField() 

    def str(self):
        return self.name