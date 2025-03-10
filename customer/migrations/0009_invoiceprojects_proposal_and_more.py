# Generated by Django 5.1.1 on 2025-01-16 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_proposalprojects_billed_proposal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceprojects',
            name='proposal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal', to='customer.proposalprojects'),
        ),
        migrations.AlterField(
            model_name='invoiceprojects',
            name='budget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='customer.budgetestimate'),
        ),
    ]
