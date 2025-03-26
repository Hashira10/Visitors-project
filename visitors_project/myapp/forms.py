from django import forms
from .models import Visitor

class CustomDateInput(forms.DateInput):
    input_type = 'text'

    def __init__(self, *args, **kwargs):
        kwargs['format'] = '%d.%m.%Y'  
        super().__init__(*args, **kwargs)

class CustomTimeInput(forms.TimeInput):
    input_type = 'time' 

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['full_name', 'organization', 'recipient_full_name', 'recipient_department']
        widgets = {
            'visit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'visit_time': CustomTimeInput(attrs={'class': 'form-control'}),
            'recipient_department': forms.Select(attrs={'class': 'form-control'}),  
        }
