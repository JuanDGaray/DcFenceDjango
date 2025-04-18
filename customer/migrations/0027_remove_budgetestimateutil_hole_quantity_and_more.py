# Generated by Django 5.1.1 on 2025-03-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0026_remove_budgetestimateutil_total_ft_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetestimateutil',
            name='hole_quantity',
        ),
        migrations.AddField(
            model_name='budgetestimateutil',
            name='profit_value_installation',
            field=models.DecimalField(decimal_places=2, default=140, max_digits=10),
        ),
        migrations.AddField(
            model_name='budgetestimateutil',
            name='profit_value_installation_check',
            field=models.BooleanField(default=False),
        ),
    ]
