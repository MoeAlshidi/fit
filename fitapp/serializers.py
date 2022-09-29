from rest_framework import serializers
from .models import Customer,Measurement, Media

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
        
        
class CustomerImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        customer_id=self.context['customer_id']
        return Media.objects.create(customer_id=customer_id,**validated_data)

    class Meta:
        model=Media
        fields=['id','image','type','customer_id']