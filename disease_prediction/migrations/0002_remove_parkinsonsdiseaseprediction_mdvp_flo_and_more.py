# Generated by Django 5.0.1 on 2024-01-29 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease_prediction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkinsonsdiseaseprediction',
            name='mdvp_flo',
        ),
        migrations.RemoveField(
            model_name='parkinsonsdiseaseprediction',
            name='mdvp_jitter_abs',
        ),
    ]
