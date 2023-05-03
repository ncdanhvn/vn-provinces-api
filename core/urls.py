from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register('regions', views.RegionViewSet)
router.register('provinces', views.ProvinceViewSet)
router.register('districts', views.DistrictViewSet)
router.register('wards', views.WardViewSet)

urlpatterns = router.urls
