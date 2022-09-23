from rest_framework import serializers
from .models import Customer,Measurement


class MeasurementsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Measurement
        fields=['id','date','weight','bust','calves','chest','waist','customer']
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','user', 'age','height']
        
