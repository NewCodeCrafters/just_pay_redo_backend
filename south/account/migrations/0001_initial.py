# Generated by Django 5.1.3 on 2024-12-07 00:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('account_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('account_number', models.PositiveBigIntegerField(blank=True, null=True, unique=True)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('NGN', 'NGN')], max_length=5)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('interest_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_transaction_date', models.DateTimeField(blank=True, null=True)),
                ('withdrawal_limit', models.DecimalField(decimal_places=2, default=1000000, max_digits=10)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]