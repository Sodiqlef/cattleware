# Generated by Django 4.0.2 on 2023-11-01 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cattle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('price', models.IntegerField(default=0)),
                ('birth_date', models.DateTimeField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('sold', models.BooleanField(default=False)),
                ('Dead', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=255)),
                ('date_given', models.DateField()),
                ('next_due_date', models.DateField()),
                ('cattle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cattle')),
            ],
        ),
        migrations.CreateModel(
            name='HealthRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('condition', models.CharField(max_length=255)),
                ('treatment', models.TextField()),
                ('cattle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cattle')),
            ],
        ),
        migrations.CreateModel(
            name='DueDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sire', models.CharField(max_length=255)),
                ('exposed_to_sire_date', models.DateField()),
                ('estimated_calving_date', models.DateField()),
                ('cattle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cattle')),
            ],
        ),
        migrations.CreateModel(
            name='BreedingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mate', models.CharField(max_length=255)),
                ('breeding_date', models.DateField()),
                ('expected_calving_date', models.DateField()),
                ('cattle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cattle')),
            ],
        ),
    ]
