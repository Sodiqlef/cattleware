from django import forms
from .models import Cattle, HealthRecord, Vaccination, BreedingRecord, DueDate



class CattleForm(forms.ModelForm):
    # Add placeholder text to specific fields
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter cattle name'}))
    breed = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter cattle breed'}))
    birth_date = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'Enter birth date in format 10/10/10'}))
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter cattle age'}))
    weight = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter cattle weight'}))
    price = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter cattle price'}))

    class Meta:
        model = Cattle
        fields = ['name', 'breed', 'birth_date', 'age',
                  'weight', 'image', 'price', 'gender']
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


class DueDateForm(forms.ModelForm):
    class Meta:
        model = DueDate
        fields = ['sire_breed', 'exposed_to_sire_date']

    def __init__(self, *args, **kwargs):
        super(DueDateForm, self).__init__(*args, **kwargs)

    exposed_to_sire_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = DueDate
        fields = [ 'sire_breed', 'exposed_to_sire_date']
        

