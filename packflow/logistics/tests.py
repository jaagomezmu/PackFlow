from django.test import TestCase
from django.urls import reverse

from .forms import PackageByCarrierForm
from .models import Carrier, Customer, Package


class CustomerPackagesViewTest(TestCase):
    def setUp(self):
        self.customer1 = Customer.objects.create(name='John Doe',
                                                 address='123 Main St',
                                                 phone_number='555-1234')
        self.carrier1 = Carrier.objects.create(name='Carrier 1',
                                               vehicle_type='Van',
                                               contact_number='+222 345')
        self.package1 = Package.objects.create(
            customer=self.customer1,
            weight=10.5,
            dimensions='20x10x5',
            origin_address='456 Elm St',
            destination_address='789 Oak St',
            delivery_status='In Transit',
            carrier=self.carrier1
        )

    def test_customer_packages_view(self):
        response = self.client.get(reverse('logistics:customer_packages'),
                                   {'customer': self.customer1.pk})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{self.package1.delivery_status}')


class CarrierPackageViewTest(TestCase):
    def setUp(self):
        self.customer1 = Customer.objects.create(name='John Doe',
                                                 address='123 Main St',
                                                 phone_number='555-1234')
        self.carrier1 = Carrier.objects.create(name='Carrier 1',
                                               vehicle_type='Van',
                                               contact_number='+222 345')
        self.package1 = Package.objects.create(
            customer=self.customer1,
            weight=10.5,
            dimensions='20x10x5',
            origin_address='456 Elm St',
            destination_address='789 Oak St',
            delivery_status='In Transit',
            carrier=self.carrier1,
        )
        self.package2 = Package.objects.create(
            customer=self.customer1,
            weight=2.5,
            dimensions='20x10x5',
            origin_address='456 Elm St',
            destination_address='789 Oak St',
            delivery_status='2 - In Transit',
            carrier=self.carrier1,
        )

    def test_get_queryset(self):
        response = self.client.get(reverse('logistics:carrier_packages'),
                                   {'carrier': self.carrier1.pk})
        form = response.context['form']
        packages = response.context['packages']

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(form, PackageByCarrierForm)
        self.assertQuerysetEqual(
            packages, [self.package1, self.package2], ordered=False)


class PackageListViewTest(TestCase):
    def test_package_list_view(self):
        url = reverse('logistics:package_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logistics/package_list.html')


class PackageCreateViewTest(TestCase):
    def test_package_create_view(self):
        url = reverse('logistics:package_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logistics/package_create.html')

    def test_package_create_view_post(self):
        url = reverse('logistics:package_create')
        data = {
            'customer': 'Customer Name',
            'weight': 10.5,
            'dimensions': '10x10x10',
            'origin_address': 'Origin Address',
            'destination_address': 'Destination Address',
            'delivery_status': 'Pending',
            'carrier': 'Carrier Name',
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)


class PackageUpdateViewTest(TestCase):
    def setUp(self):
        self.customer1 = Customer.objects.create(name='John Doe',
                                                 address='123 Main St',
                                                 phone_number='555-1234')
        self.carrier1 = Carrier.objects.create(name='Carrier 1',
                                               vehicle_type='Van',
                                               contact_number='+222 345')
        self.package = Package.objects.create(
            customer=self.customer1,
            weight=10.5,
            dimensions='10x10x10',
            origin_address='Origin Address',
            destination_address='Destination Address',
            delivery_status='Pending',
            carrier=self.carrier1,
        )

    def test_package_update_view(self):
        url = reverse('logistics:package_update', args=[self.package.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_package_update_view_post(self):
        url = reverse('logistics:package_update', args=[self.package.pk])
        data = {
            'customer': 'Updated Customer Name',
            'weight': 12.3,
            'dimensions': '12x12x12',
            'origin_address': 'Updated Origin Address',
            'destination_address': 'Updated Destination Address',
            'delivery_status': 'Delivered',
            'carrier': 'Updated Carrier Name',
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)

class PackageDeleteViewTest(TestCase):
    def setUp(self):
        self.customer1 = Customer.objects.create(name='John Doe',
                                                 address='123 Main St',
                                                 phone_number='555-1234')
        self.carrier1 = Carrier.objects.create(name='Carrier 1',
                                               vehicle_type='Van',
                                               contact_number='+222 345')
        self.package = Package.objects.create(
            customer=self.customer1,
            weight=10.5,
            dimensions='10x10x10',
            origin_address='Origin Address',
            destination_address='Destination Address',
            delivery_status='Pending',
            carrier=self.carrier1,
        )

    def test_package_delete_view(self):
        url = reverse('logistics:package_delete', args=[self.package.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logistics/package_delete.html')

    def test_package_delete_view_post(self):
        url = reverse('logistics:package_delete', args=[self.package.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('logistics:package_list'))
        self.assertFalse(Package.objects.filter(pk=self.package.pk).exists())
