from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('cattle/', views.cattle_list, name='cattle_list'),
    path('cattle/<int:pk>/', views.cattle_detail, name='cattle_detail'),
    path('cattle/add/', views.add_cattle, name='add_cattle'),
    path('cattle/edit/<int:pk>/', views.edit_cattle, name='edit_cattle'),
    # Add similar URL patterns for HealthRecord, Vaccination, and BreedingRecord views
    # path('healthrecord/add/', views.add_health_record, name='add_health_record'),
    # path('healthrecord/edit/<int:pk>/', views.edit_health_record, name='edit_health_record'),


]