from rest_framework import serializers
from .models import Customer,Measurement

class MeasurementsSerializer(serializers.ModelSerializer):
    customer_id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Measurement
        fields=['id','date','weight','bust','calves','chest','waist','customer_id']
        
        
class CustomerSerializer(serializers.ModelSerializer):
    user_id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Customer
        fields=['id','user_id', 'age','height','created_on']
        
class UpdateCustomerSerializer(serializers.ModelSerializer):
    user_id=serializers.PrimaryKeyRelatedField(read_only=True)
    created_on=serializers.DateTimeField(read_only=True)
    class Meta:
        model=Customer
        fields=['user_id','age','height','created_on']
        
        
class HomeSerializer(serializers.ModelSerializer):
    measurements=MeasurementsSerializer(many=True)
    class Meta:
        model=Customer
        fields=['user_id','age','height','created_on','measurements']
        
    