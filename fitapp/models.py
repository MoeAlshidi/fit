from django.db import models
from django.conf import settings

# Create your models here.
class Measurement(models.Model):
    
    pass



class Media(models.Model):
    TYPE_FRONT='F'
    TYPE_BACK='B'
    TYPE_SIDE='S'
    TYPE_CHOICES=[
        (TYPE_FRONT,'Front'),
        (TYPE_BACK,'Back'),
        (TYPE_SIDE,'Side'),
    ]


class Customer(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    measurement=models.ForeignKey(Measurement,on_delete=models.CASCADE,related_name='measurements')



