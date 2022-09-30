from datetime import date, datetime, timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Measurement, Media
from .serializers import CustomerSerializer, MeasurementsSerializer, UpdateCustomerSerializer, CustomerImageSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home_view(request):
    week_start = timezone.now()
    week_start -= timedelta(days=week_start.weekday())
    week_end = week_start + timedelta(days=6)
    user = request.user

    current_customer = Customer.objects.only('id') \
        .get(user_id=user.id)
    customer = Customer.objects.filter(id=current_customer.id)
    customer_serializer = CustomerSerializer(customer, many=True)
    measurement = Measurement.objects.filter(customer_id=current_customer.id, date__range=[week_start, week_end])
    measurement_serializer = MeasurementsSerializer(measurement, many=True)
    images = Media.objects.filter(customer_id=current_customer.id, date__range=[week_start, week_end])
    images_serializer = CustomerImageSerializer(images, many=True)
    return Response(
        data={
            'code': status.HTTP_200_OK,
            'data': {
                'user': customer_serializer.data,
                'measurements': measurement_serializer.data,
                'images': images_serializer.data,
            }
        }

    )


class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'])
    def current(self, request):
        customer = Customer.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = UpdateCustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user_id=user.id)


class MeasurementViewSet(ModelViewSet):
    http_method_names = ['get', 'put', 'post']
    serializer_class = MeasurementsSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        week_start = timezone.now()
        week_start -= timedelta(days=week_start.weekday())
        week_end = week_start + timedelta(days=6)
        user = self.request.user
        customer = Customer.objects.only('id').get(user_id=user.id)
        has_measurements = Measurement.objects.filter(customer_id=customer.id, date__range=[week_start, week_end])
        if has_measurements.exists():
            return Response('Measurements For This Week Is Already Added', status=status.HTTP_204_NO_CONTENT)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        customer = Customer.objects.only('id').get(user_id=user.id)
        serializer.save(customer_id=customer.id)

    def get_queryset(self):
        user = self.request.user
        customer = Customer.objects.only('id').get(user_id=user.id)
        return Measurement.objects.filter(customer_id=customer.id)


class CustomerImageViewSet(ModelViewSet):
    serializer_class = CustomerImageSerializer

    def get_serializer_context(self):
        user = self.request.user
        customer = Customer.objects.only('id').get(user_id=user.id)
        return {'customer_id': customer.id}

    def get_queryset(self):
        user = self.request.user
        customer = Customer.objects.only('id').get(user_id=user.id)
        return Media.objects.filter(customer_id=customer.id)
