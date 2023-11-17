from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('cattle/', views.cattle_list, name='cattle_list'),
    path('cattle/<int:pk>/', views.cattle_detail, name='cattle_detail'),
    path('cattle/add/', views.add_cattle, name='add_cattle'),
    path('cattle/edit/<int:pk>/', views.edit_cattle, name='edit_cattle'),
    path('due_date/add/<int:cattle_id>/', views.add_due_date, name='add_due_date'),
    path('cattle/delete/<int:cattle_id>/',views.delete_cattle, name='delete_cattle'),
    path('healthrecord/add/<int:cattle_id>/', views.add_hr, name='add_health_record'),
    path('healthrecord/edit/<int:pk>/', views.edit_hr, name='edit_health_record'),
    path('vaccination/add/', views.add_vr, name='add_vr'),
    path('vaccination/edit/<int:pk>/', views.edit_vr, name='edit_vr'),


]