from django.db import models

# Create your models here.


class Cattle(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[
                              ('Male', 'Male'), ('Female', 'Female')])
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    # Assuming you have user authentication
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HealthRecord(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    date = models.DateField()
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


class BreedingRecord(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    mate = models.CharField(max_length=255)
    breeding_date = models.DateField()
    expected_calving_date = models.DateField()

    def __str__(self):
        return f"{self.cattle.name}'s Breeding Record with {self.mate}"


