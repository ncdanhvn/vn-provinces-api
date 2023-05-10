from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register('regions', views.RegionViewSet, basename='regions')
router.register('provinces', views.ProvinceViewSet, basename='provinces')
router.register('districts', views.DistrictViewSet)
router.register('wards', views.WardViewSet)

# other_urls = [
#     path('hello/', views.say_hello)
# ]

# urlpatterns = router.urls + other_urls

urlpatterns = router.urls
