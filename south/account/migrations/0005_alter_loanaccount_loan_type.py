# Generated by Django 5.1.3 on 2024-12-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_loanaccount_id_loanaccount_loan_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanaccount',
            name='loan_type',
            field=models.CharField(choices=[('personal', 'Personal Loan'), ('business', 'Business Loan'), ('education', 'Education Loan')], max_length=20),
        ),
    ]
