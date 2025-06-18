from django import forms
from .models import ApplicationModel


class ApplicationForm(forms.ModelForm):
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
        self.fields["name"].widget.attrs.update({"class": "form-control"})