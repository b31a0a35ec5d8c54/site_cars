from django.forms import ModelForm
from .models import Car

# Create the form class.
class VehicleForm(ModelForm):
    class Meta:
        model = Car
        # fields = ['created', 'vin']
        fields = ['vin']


from django import forms

class UploadVehicleFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
    file = forms.FileField()
        
