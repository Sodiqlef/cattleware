from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import timedelta
from .models import Cattle, DueDate, HealthRecord, Vaccination, BreedingRecord
from .forms import CattleForm, HealthRecordForm, VaccinationForm, BreedingRecordForm, DueDateForm
from blog.models import BlogPost


# Create your views here.
def calculate_due_date(exposure_date, sire_breed):

    breed_gestation_periods = {
        'Angus': 280,
        'Hereford': 270,
        'Holstein': 279,
        'Limousin': 280,
        'Simmental': 285,
        'Charolais': 282,
        'Jersey': 278,
    
    }

    # Get the gestation period for the provided sire's breed, default to 275 days if not found
    gestation_period = breed_gestation_periods.get(sire_breed, 275)
    estimated_calving_date = exposure_date + timedelta(days=gestation_period)

    return estimated_calving_date



def home(request):
    recent_blogs = BlogPost.objects.all().order_by('-pub_date')[:3]
    user = User.objects.all().count()
    cattle = Cattle.objects.all().count()
    return render(request, 'index.html', {"recent_blogs": recent_blogs, 'user':user, 'cattle': cattle})


@login_required
def cattle_list(request):
    # Get the search query from the request
    search_query = request.GET.get('search', '')

    # Filter cattle records based on the search query and owner
    cattle_records = Cattle.objects.filter(
        owner=request.user, name__icontains=search_query).order_by('-pub_date')

    return render(request, 'cattle_list.html', {'cattle_records': cattle_records, 'search_query': search_query})



def cattle_detail(request, pk):
    cattle_record = Cattle.objects.get(pk=pk)
    return render(request, 'cattle_detail.html', {'cattle_record': cattle_record})


def add_cattle(request):
    if request.method == 'POST':
        form = CattleForm(request.POST, request.FILES)
        if form.is_valid():
            new_cattle = form.save(commit=False)
            new_cattle.owner = request.user
            new_cattle.save()
            messages.success(request, 'Your cattle was updated successfully!')
            return redirect('cattle_list')
        else:
            messages.error(request, 'Your cattle was not uploaded.')
    else:
        form = CattleForm()
    return render(request, 'add_cattle.html', {'form': form})


@login_required
def delete_cattle(request, cattle_id):
    cattle = get_object_or_404(Cattle, id=cattle_id)

    if request.user == cattle.owner:
        cattle.delete()
        messages.warning(request, 'Cattle has been deleted successfully')
        return redirect('cattle_list')
    else:
        return HttpResponseForbidden("You do not have permission to delete this cattle record.")


def edit_cattle(request, pk):
    cattle_record = Cattle.objects.get(pk=pk)
    if request.method == 'POST':
        form = CattleForm(request.POST, instance=cattle_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cattle has been edited successfully')
            return redirect('cattle_detail', pk=pk)
        else:
            messages.error(request, 'An error occured')
    else:
        form = CattleForm(instance=cattle_record)
    return render(request, 'edit_cattle.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def add_due_date(request, cattle_id):
    if request.method == "POST" :

        form = DueDateForm(request.POST)
        if form.is_valid():
            cattle = Cattle.objects.get(pk=cattle_id)
            sire_breed = form.cleaned_data['sire_breed']
            exposure_date = form.cleaned_data['exposed_to_sire_date']
            estimated_calving_date = calculate_due_date(
                exposure_date, sire_breed)

            due_date = DueDate(cattle=cattle, sire_breed=sire_breed, exposed_to_sire_date=exposure_date,
                            estimated_calving_date=estimated_calving_date)
            due_date.save()
            messages.success(request, 'Due date successfully updated')

            return redirect('cattle_list')
    else:
        form = DueDateForm()
    
    return render(request, 'due_date.html', {'form': form })
