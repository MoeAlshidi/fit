from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Measurement
from .serializers import CustomerSerializer,MeasurementsSerializer,UpdateCustomerSerializer, HomeSerializer


class HomeViewSet(ModelViewSet):
    serializer_class=HomeSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        customer=Customer.objects.only('id').get(user_id=user.id)
        return Customer.objects.filter(id=customer.id)
    

class CustomerViewSet(CreateModelMixin, RetrieveModelMixin,UpdateModelMixin, GenericViewSet):
    serializer_class=CustomerSerializer
    permission_classes=[IsAuthenticated]
    @action(detail=False,methods=['GET','PUT'])
    def current(self, request):
        customer=Customer.objects.get(user_id=request.user.id, )

        if request.method=='GET':
            serializer=CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=UpdateCustomerSerializer(customer,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
            
            #TODO Go through the api design one more
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user_id=user.id)


class MeasurementViewSet(ModelViewSet):
    http_method_names=['get','put','post']
    serializer_class=MeasurementsSerializer
    permission_classes=[IsAuthenticated]
    queryset=Measurement.objects.all()
    
    #TODO Before creating the measurements make sure there are no measurements this week.
    #TODO //
    
    def perform_create(self, serializer):
        user=self.request.user
        customer=Customer.objects.only('id').get(user_id=user.id)
        serializer.save(customer_id=customer.id)
    def get_queryset(self):
        user=self.request.user
        customer=Customer.objects.only('id').get(user_id=user.id)
        return Measurement.objects.filter(customer_id=customer.id)
