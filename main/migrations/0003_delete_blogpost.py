# Generated by Django 4.0.2 on 2023-09-23 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blogpost_approve'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]