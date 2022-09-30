from . import views
from django.urls import path
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('customer', views.CustomerViewSet, basename='customer')
router.register('measurements', views.MeasurementViewSet, basename='measurements')
router.register('media', views.CustomerImageViewSet, basename='media')
router.register('hydration', views.HydrationViewSet, basename='hydration')

customer_router = routers.NestedSimpleRouter(router, 'customer', lookup='customer')

urlpatterns = [
                  path('home/', views.home_view, name='home')
              ] + router.urls
