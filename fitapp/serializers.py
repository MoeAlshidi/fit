from rest_framework import serializers
from .models import Customer,Measurement

class MeasurementsSerializer(serializers.ModelSerializer):
    customer_id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Measurement
        fields=['id','date','weight','bust','calves','chest','waist','customer_id']
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','user', 'age','height']
        
