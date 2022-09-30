from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

class Measurement(models.Model):
    
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE, default=None,related_name='measurements')
    weight=models.PositiveSmallIntegerField(blank=False)
    bust=models.DecimalField(max_digits=5, decimal_places=2,blank=False)
    calves=models.DecimalField(max_digits=5, decimal_places=2,blank=False)
    chest=models.DecimalField(max_digits=5, decimal_places=2,blank=False)
    waist=models.DecimalField(max_digits=5,decimal_places=2,blank=False)
    date=models.DateTimeField(blank=False, default=None,null=False)
    
    class Meta:
        ordering=['-date']
    
class Customer(models.Model):
    
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age=models.PositiveIntegerField(blank=True,null=True)
    height=models.PositiveIntegerField(blank=True,null=True)
    created_on=models.DateTimeField(auto_now_add=True)
    
    def email(self):
        return self.user.email
    def first_name(self):
        return self.user.first_name
    def last_name(self):
        return self.user.last_name


class Media(models.Model):
    TYPE_FRONT='F'
    TYPE_BACK='B'
    TYPE_SIDE='S'
    TYPE_CHOICES=[
        (TYPE_FRONT,'Front'),
        (TYPE_BACK,'Back'),
        (TYPE_SIDE,'Side'),
    ]
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='images')
    image=ResizedImageField(upload_to='fit/images')
    type=models.CharField(max_length=1,choices=TYPE_CHOICES, default=None)
    date=models.DateTimeField(auto_now_add=True)
    


