from django.urls import path

from .views import (CarrierPackagesView, CustomerPackagesView,
                    PackageCreateView, PackageDeleteView, 
                    PackageListView, PackageUpdateView)

app_name = 'logistics'

urlpatterns = [
    path('customer_packages/', CustomerPackagesView.as_view(), name='customer_packages'),
    path('carrier_packages/', CarrierPackagesView.as_view(), name='carrier_packages'),
    path('package-list/', PackageListView.as_view(), name='package_list'),
    path('package/create/', PackageCreateView.as_view(), name='package_create'),
    path('package/update/<int:pk>/', PackageUpdateView.as_view(), name='package_update'),
    path('package/delete/<int:pk>/', PackageDeleteView.as_view(), name='package_delete'),
]

