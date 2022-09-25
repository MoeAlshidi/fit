from . import views
from rest_framework_nested import routers


router=routers.DefaultRouter()

router.register('customer',views.CustomerViewSet,basename='customer')
customer_router=routers.NestedSimpleRouter(router,'customer',lookup='customer')
router.register('measurements',views.MeasurementViewSet)



urlpatterns = router.urls
