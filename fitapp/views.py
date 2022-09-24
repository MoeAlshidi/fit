from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin,UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Measurement
from .serializers import CustomerSerializer,MeasurementsSerializer



class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,GenericViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes=[IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        exist=Customer.objects.get(user_id=self.request.user.id)
        print(exist)
        if exist==None:
            self.serializer.save(user_id=self.request.user.id)  
            return Response(self.serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('Customer Already Exist', status=status.HTTP_400_BAD_REQUEST)


      


        


class MeasurementViewSet(ModelViewSet):
    http_method_names=['get','put','post']
    serializer_class=MeasurementsSerializer
    permission_classes=[IsAuthenticated]
    queryset=Measurement.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(customer_id=self.request.user.id)
    def get_queryset(self):
        return Measurement.objects.filter(customer_id=self.request.user.id)
