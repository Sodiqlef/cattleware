from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cattle, HealthRecord, Vaccination, BreedingRecord
from .forms import CattleForm, HealthRecordForm, VaccinationForm, BreedingRecordForm
from blog.models import BlogPost


# Create your views here.


def home(request):
    recent_blogs = BlogPost.objects.all().order_by('-pub_date')[:3]
    return render(request, 'index.html', {"recent_blogs": recent_blogs})



@login_required
def cattle_list(request):
    cattle_records = Cattle.objects.filter(owner=request.user).order_by('-pub_date')
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


def profile(request):
    return render(request, 'profile.html')