from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.


class Cattle(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    image = CloudinaryField('image', transformation=[ 
        {'width': 192, 'height': 124, 'crop': 'fill'}], null=True)
    price = models.IntegerField(default=0)
    birth_date = models.DateTimeField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    gender = models.CharField(max_length=10, choices=[
                              ('Male', 'Male'), ('Female', 'Female')])
    sold = models.BooleanField(default=False)
    Dead = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.name


class HealthRecord(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    condition = models.CharField(max_length=255)
    treatment = models.TextField()
    def __str__(self):
        return f"{self.cattle.name}'s Health Record on {self.date}"


class Vaccination(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=255)
    date_given = models.DateField()
    next_due_date = models.DateField()

    def __str__(self):
        return f"{self.cattle.name}'s {self.vaccine_name} Vaccination"


class DueDate(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE, related_name='duedate')
    sire_breed = models.CharField(max_length=255)
    exposed_to_sire_date = models.DateField()
    estimated_calving_date = models.DateField()

    def __str__(self):
        return f"{self.cattle.name}'s Due Date with {self.sire}"
