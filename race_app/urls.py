from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, garage , winners

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('garage/', garage, name='garage'),  # HTML view for garage
    path('winners/', winners, name='winners'),
]