# Generated by Django 4.0.2 on 2023-10-05 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_cattle_for_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cattle',
            name='for_sale',
        ),
    ]