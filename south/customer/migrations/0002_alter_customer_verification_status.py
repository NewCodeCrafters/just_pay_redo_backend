# Generated by Django 5.1.3 on 2024-12-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='verification_status',
            field=models.CharField(choices=[('passport', 'Passport'), ('national_id', 'National ID'), ('driver_license', 'Driver License')], max_length=40),
        ),
    ]
