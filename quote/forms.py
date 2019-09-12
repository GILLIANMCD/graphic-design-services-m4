from django import forms
from .models import Quote

class GetQuote(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('full_name', 'position', 'company', 'phone_number', 'email', 
                    'town_or_city', 'street_address1', 'street_address2', 
                    'county', 'country', 'postcode', 'message', 'image', 'service_required')
