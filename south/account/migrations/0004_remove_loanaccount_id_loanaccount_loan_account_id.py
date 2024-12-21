# Generated by Django 5.1.3 on 2024-12-12 22:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_loanaccount_delete_accounts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanaccount',
            name='id',
        ),
        migrations.AddField(
            model_name='loanaccount',
            name='loan_account_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
