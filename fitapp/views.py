from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,ListModelMixin
from .models import Customer, Measurement
from .serializers import CustomerSerializer,MeasurementsSerializer




# Create your views here.
class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,GenericViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    


class MeasurementViewSet(ModelViewSet):
    http_method_names=['get','post', 'put']
    serializer_class=MeasurementsSerializer
    queryset=Measurement.objects.all()
    

