from django.views.generic import ListView
from django.views.generic.edit import (CreateView, DeleteView, FormMixin,
                                       UpdateView)

from .forms import PackageByCarrierForm, PackageByCustomerForm, PackageForm
from .models import Carrier, Package


class CustomerPackagesView(ListView, FormMixin):
    model = Package
    template_name = 'logistics/customer_packages.html'
    context_object_name = 'packages'
    form_class = PackageByCustomerForm
    
    def get_queryset(self):
        customer = self.request.GET.get('customer')
        return Package.objects.filter(customer_id=customer)

class CarrierPackagesView(ListView, FormMixin):
    model = Carrier
    template_name = 'logistics/carrier_packages.html'
    context_object_name = 'packages'
    form_class = PackageByCarrierForm

    def get_queryset(self):
        carrier = self.request.GET.get('carrier')
        return Package.objects.filter(carrier__id=carrier)

class PackageListView(ListView):
    model = Package
    template_name = 'logistics/package_list.html'
    context_object_name = 'packages'

class PackageCreateView(CreateView):
    model = Package
    form_class = PackageForm
    template_name = 'logistics/package_create.html'
    success_url = '/logistics/package-list/'

class PackageUpdateView(UpdateView):
    model = Package
    form_class = PackageForm
    template_name = 'logistics/package_update.html'
    success_url = '/logistics/package-list/'

class PackageDeleteView(DeleteView):
    model = Package
    template_name = 'logistics/package_delete.html'
    success_url = '/logistics/package-list/'

