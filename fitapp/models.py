from django.db import models
from datetime import datetime    
from django.conf import settings

# Create your models here.
class Measurement(models.Model):
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE, default=None,related_name='customers')
    weight=models.PositiveSmallIntegerField(blank=False)
    bust=models.DecimalField(max_digits=5, decimal_places=2,blank=False)
    calves=models.DecimalField(max_digits=5, decimal_places=2,blank=False)
    chest=models.DecimalField(max_digits=5, decimal_places=2,blank=False)
    waist=models.DecimalField(max_digits=5,decimal_places=2,blank=False)
    date=models.DateTimeField( blank=True, default=None)
    

# class Media(models.Model):
#     TYPE_FRONT='F'
#     TYPE_BACK='B'
#     TYPE_SIDE='S'
#     TYPE_CHOICES=[
#         (TYPE_FRONT,'Front'),
#         (TYPE_BACK,'Back'),
#         (TYPE_SIDE,'Side'),
#     ]


class Customer(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age=models.PositiveIntegerField(blank=False,null=True)
    height=models.PositiveIntegerField(blank=False,null=True)
    created_on=models.DateTimeField(auto_now_add=True)
  
    # media=models.ForeignKey(Media,on_delete=models.CASCADE, related_name='media')
    
    def __str__(self):
        return self.user.first_name
    
    
    def email(self):
        return self.user.email
    def first_name(self):
        return self.user.first_name
    def last_name(self):
        return self.user.last_name



