from django import forms
from .models import Cattle, HealthRecord, Vaccination, BreedingRecord


class CattleForm(forms.ModelForm):
    class Meta:
        model = Cattle
        fields = ['name', 'breed', 'date_of_birth', 'gender', 'weight']
        # You can customize the fields as needed


class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['cattle', 'date', 'condition', 'treatment']
        

class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ['cattle', 'vaccine_name', 'date_given', 'next_due_date']


class BreedingRecordForm(forms.ModelForm):
    class Meta:
        model = BreedingRecord
        fields = ['cattle', 'mate', 'breeding_date', 'expected_calving_date']
        
