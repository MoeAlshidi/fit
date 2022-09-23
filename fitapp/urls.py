from . import views
from rest_framework_nested import routers


router=routers.DefaultRouter()

router.register('customers',views.CustomerViewSet,basename='customers')
customer_router=routers.NestedSimpleRouter(router,'customers',lookup='customer')
router.register('measurements',views.MeasurementViewSet)



urlpatterns = router.urls
