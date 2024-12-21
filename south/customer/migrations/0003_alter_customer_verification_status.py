# Generated by Django 5.1.3 on 2024-12-17 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_verification_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='verification_status',
            field=models.CharField(choices=[('national_id', 'National ID'), ('driver_license', 'Driver License'), ('passport', 'Passport')], max_length=40),
        ),
    ]
