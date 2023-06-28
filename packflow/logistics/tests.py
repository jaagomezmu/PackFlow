from django.test import TestCase
from django.urls import reverse
from logistics.api.serializers import (CarrierSerializer, CustomerSerializer,
                                       PackageSerializer)
from rest_framework import status
from rest_framework.test import APIClient

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

class PackageViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer1 = Customer.objects.create(
            name='John Doe',
            address='Address 1',
            phone_number='123456789'
        )
        self.customer2 = Customer.objects.create(
            name='Jane Smith',
            address='Address 2',
            phone_number='987654321'
        )
        self.carrier1 = Carrier.objects.create(
            name='Carrier 1',
            vehicle_type='Truck',
            contact_number='555-1234'
        )
        self.carrier2 = Carrier.objects.create(
            name='Carrier 2',
            vehicle_type='Van',
            contact_number='555-5678'
        )
        self.package1 = Package.objects.create(
            customer=self.customer1,
            weight=10.0,
            dimensions='20x30x40',
            origin_address='Address 3',
            destination_address='Address 4',
            delivery_status='Pending',
            carrier=self.carrier1
        )
        self.package2 = Package.objects.create(
            customer=self.customer2,
            weight=5.0,
            dimensions='15x25x35',
            origin_address='Address 5',
            destination_address='Address 6',
            delivery_status='Delivered',
            carrier=self.carrier2
        )

    def test_get_all_packages(self):
        url = reverse('logistics:package-list')
        response = self.client.get(url)
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_package(self):
        url = reverse('logistics:package-detail', args=[self.package1.pk])
        response = self.client.get(url)
        package = Package.objects.get(pk=self.package1.pk)
        serializer = PackageSerializer(package)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_package(self):
        url = reverse('logistics:package-list')
        data = {
            'customer': self.customer1.pk,
            'weight': 8.0,
            'dimensions': '25x35x45',
            'origin_address': 'Address 7',
            'destination_address': 'Address 8',
            'delivery_status': 'Pending',
            'carrier': self.carrier1.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Package.objects.count(), 3)

    def test_update_package(self):
        url = reverse('logistics:package-detail', args=[self.package1.pk])
        data = {
            'dimensions': '30x40x50',
        }
        response = self.client.patch(url, data, format='json')
        package = Package.objects.get(pk=self.package1.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(package.dimensions, '30x40x50')

    def test_delete_package(self):
        url = reverse('logistics:package-detail', args=[self.package1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Package.objects.count(), 1)

class CarrierViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer1 = Customer.objects.create(
            name='John Doe',
            address='Address 1',
            phone_number='123456789'
        )
        self.customer2 = Customer.objects.create(
            name='Jane Smith',
            address='Address 2',
            phone_number='987654321'
        )
        self.carrier1 = Carrier.objects.create(
            name='Carrier 1',
            vehicle_type='Truck',
            contact_number='555-1234'
        )
        self.carrier2 = Carrier.objects.create(
            name='Carrier 2',
            vehicle_type='Van',
            contact_number='555-5678'
        )
        self.package1 = Package.objects.create(
            customer=self.customer1,
            weight=10.0,
            dimensions='20x30x40',
            origin_address='Address 3',
            destination_address='Address 4',
            delivery_status='Pending',
            carrier=self.carrier1
        )
        self.package2 = Package.objects.create(
            customer=self.customer2,
            weight=5.0,
            dimensions='15x25x35',
            origin_address='Address 5',
            destination_address='Address 6',
            delivery_status='Delivered',
            carrier=self.carrier2
        )

    def test_get_all_carriers(self):
        url = reverse('logistics:carrier-list')
        response = self.client.get(url)
        carriers = Carrier.objects.all()
        serializer = CarrierSerializer(carriers, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_carrier(self):
        url = reverse('logistics:carrier-detail', args=[self.carrier1.pk])
        response = self.client.get(url)
        carrier = Carrier.objects.get(pk=self.carrier1.pk)
        serializer = CarrierSerializer(carrier)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_carrier(self):
        url = reverse('logistics:carrier-list')
        data = {
            'name': 'Carrier 3',
            'vehicle_type': 'Bike',
            'contact_number': '555-9999'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Carrier.objects.count(), 3)

    def test_update_carrier(self):
        url = reverse('logistics:carrier-detail', args=[self.carrier1.pk])
        data = {
            'vehicle_type': 'Car',
        }
        response = self.client.patch(url, data, format='json')
        carrier = Carrier.objects.get(pk=self.carrier1.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(carrier.vehicle_type, 'Car')

    def test_delete_carrier(self):
        url = reverse('logistics:carrier-detail', args=[self.carrier1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Carrier.objects.count(), 1)

class CustomerViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer1 = Customer.objects.create(
            name='John Doe',
            address='Address 1',
            phone_number='123456789'
        )
        self.customer2 = Customer.objects.create(
            name='Jane Smith',
            address='Address 2',
            phone_number='987654321'
        )
        self.carrier1 = Carrier.objects.create(
            name='Carrier 1',
            vehicle_type='Truck',
            contact_number='555-1234'
        )
        self.carrier2 = Carrier.objects.create(
            name='Carrier 2',
            vehicle_type='Van',
            contact_number='555-5678'
        )
        self.package1 = Package.objects.create(
            customer=self.customer1,
            weight=10.0,
            dimensions='20x30x40',
            origin_address='Address 3',
            destination_address='Address 4',
            delivery_status='Pending',
            carrier=self.carrier1
        )
        self.package2 = Package.objects.create(
            customer=self.customer2,
            weight=5.0,
            dimensions='15x25x35',
            origin_address='Address 5',
            destination_address='Address 6',
            delivery_status='Delivered',
            carrier=self.carrier2
        )

    def test_get_all_customers(self):
        url = reverse('logistics:customer-list')
        response = self.client.get(url)
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_customer(self):
        url = reverse('logistics:customer-detail', args=[self.customer1.pk])
        response = self.client.get(url)
        customer = Customer.objects.get(pk=self.customer1.pk)
        serializer = CustomerSerializer(customer)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_customer(self):
        url = reverse('logistics:customer-list')
        data = {
            'name': 'New Customer',
            'address': 'New Address',
            'phone_number': '555-9999'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 3)

    def test_update_customer(self):
        url = reverse('logistics:customer-detail', args=[self.customer1.pk])
        data = {
            'address': 'Updated Address',
        }
        response = self.client.patch(url, data, format='json')
        customer = Customer.objects.get(pk=self.customer1.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(customer.address, 'Updated Address')

    def test_delete_customer(self):
        url = reverse('logistics:customer-detail', args=[self.customer1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 1)