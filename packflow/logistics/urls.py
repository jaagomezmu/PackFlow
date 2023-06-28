from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CarrierPackagesView, CarrierViewSet, CustomerPackagesView,
                    CustomerViewSet, PackageCreateView, PackageDeleteView, 
                    PackageListView,PackageUpdateView, PackageViewSet)

app_name = 'logistics'

router = DefaultRouter()
router.register(r'packages', PackageViewSet, basename='package')
router.register(r'carriers', CarrierViewSet, basename='carrier')
router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('customer_packages/', CustomerPackagesView.as_view(), name='customer_packages'),
    path('carrier_packages/', CarrierPackagesView.as_view(), name='carrier_packages'),
    path('package-list/', PackageListView.as_view(), name='package_list'),
    path('package/create/', PackageCreateView.as_view(), name='package_create'),
    path('package/update/<int:pk>/', PackageUpdateView.as_view(), name='package_update'),
    path('package/delete/<int:pk>/', PackageDeleteView.as_view(), name='package_delete'),
    path('api/', include(router.urls)),
]

