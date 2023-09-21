from django.shortcuts import render, redirect
from .models import Cattle, HealthRecord, Vaccination, BreedingRecord
from .forms import CattleForm, HealthRecordForm, VaccinationForm, BreedingRecordForm


# Create your views here.


def home(request):
    return render(request, 'index.html')



def cattle_list(request):
    cattle_records = Cattle.objects.all()
    return render(request, 'cattle_list.html', {'cattle_records': cattle_records})


def cattle_detail(request, pk):
    cattle_record = Cattle.objects.get(pk=pk)
    return render(request, 'cattle_detail.html', {'cattle_record': cattle_record})


def add_cattle(request):
    if request.method == 'POST':
        form = CattleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cattle_list')
    else:
        form = CattleForm()
    return render(request, 'add_cattle.html', {'form': form})


def edit_cattle(request, pk):
    cattle_record = Cattle.objects.get(pk=pk)
    if request.method == 'POST':
        form = CattleForm(request.POST, instance=cattle_record)
        if form.is_valid():
            form.save()
            return redirect('cattle_detail', pk=pk)
    else:
        form = CattleForm(instance=cattle_record)
    return render(request, 'edit_cattle.html', {'form': form})

