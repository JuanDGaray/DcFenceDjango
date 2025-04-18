# Generated by Django 5.1.1 on 2025-02-06 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0022_alter_project_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealCostProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subitems', models.JSONField(default=list)),
                ('total', models.CharField(default='none', max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost_items', to='customer.project')),
            ],
        ),
    ]
