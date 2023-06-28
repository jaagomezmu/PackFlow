from django import forms
from .models import Package
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PackageByCustomerForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['customer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Search'))

class PackageByCarrierForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['carrier']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Search'))

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['customer', 'weight', 'dimensions', 'origin_address', 'destination_address', 'delivery_status', 'carrier']