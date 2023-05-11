from django.urls import path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('regions', views.RegionViewSet, basename='regions')
router.register('provinces', views.ProvinceViewSet, basename='provinces')
router.register('districts', views.DistrictViewSet)
router.register('wards', views.WardViewSet)

provinces_router = routers.NestedDefaultRouter(
    router, 'provinces', lookup='province')
provinces_router.register('wards', views.WardFromAProvinceViewSet,
                         basename='province-wards')

# other_urls = [
#     path('hello/', views.say_hello)
# ]

# urlpatterns = router.urls + other_urls

urlpatterns = router.urls
