from django import forms
from .models import InsuranceClaim

class InsuranceClaimForm(forms.ModelForm):
    class Meta:
        model = InsuranceClaim
        fields = ['hospital_name', 'treatment_details', 'document']
