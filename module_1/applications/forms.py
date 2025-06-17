from django import forms
from .models import ApplicationModel


class ApplicationModelForm(forms.ModelForm):
    
    class Meta:
        model = ApplicationModel
        fields = ("address", "contacts", "service_type", "payment_type")
        
