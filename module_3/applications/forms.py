from django import forms
from .models import ApplicationModel


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = [
            'address',
            'phone_number',
            'date_time',
            'service_type',
            'other_service_description',
            'payment_type',
            ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({"class": "form-control"})