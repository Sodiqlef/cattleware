from django.contrib import admin
from .models import Cattle, DueDate, HealthRecord, Vaccination


# Register your models here.

admin.site.register(Cattle)
admin.site.register(DueDate)
admin.site.register(HealthRecord)
admin.site.register(Vaccination)