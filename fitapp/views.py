from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Measurement
from .serializers import CustomerSerializer,MeasurementsSerializer,UpdateCustomerSerializer




class CustomerViewSet(CreateModelMixin, RetrieveModelMixin,UpdateModelMixin, GenericViewSet):
    serializer_class=CustomerSerializer
    permission_classes=[IsAuthenticated]

    
    @action(detail=False,methods=['GET','PUT'])
    def current(self, request):
        (customer, created)=Customer.objects.get_or_create(user_id=request.user.id, defaults={'age':None, 'height':None})
        if not created:
            if request.method=='GET':
                serializer=CustomerSerializer(customer)
                return Response(serializer.data)
            elif request.method=='PUT':
                serializer=UpdateCustomerSerializer(customer,data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(data={
                'code':status.HTTP_400_BAD_REQUEST,
                'data':'Customer is Already Created'}, status=status.HTTP_400_BAD_REQUEST)
            
            #TODO Go through the api design one more time.
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class MeasurementViewSet(ModelViewSet):
    http_method_names=['get','put','post']
    serializer_class=MeasurementsSerializer
    permission_classes=[IsAuthenticated]
    queryset=Measurement.objects.all()
    
    #TODO Before creating the measurements make sure there are no measurements this week.
    #TODO //
    
    def perform_create(self, serializer):
        serializer.save(customer_id=self.request.user.id)
    def get_queryset(self):
        return Measurement.objects.filter(customer_id=self.request.user.id)
