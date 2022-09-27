from . import views
from rest_framework_nested import routers


router=routers.DefaultRouter()

router.register('customer',views.CustomerViewSet,basename='customer')
router.register('home',views.HomeViewSet,basename='home')
router.register('measurements',views.MeasurementViewSet)
customer_router=routers.NestedSimpleRouter(router,'customer',lookup='customer')




urlpatterns = router.urls
