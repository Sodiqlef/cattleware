# Generated by Django 4.0.2 on 2023-09-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]