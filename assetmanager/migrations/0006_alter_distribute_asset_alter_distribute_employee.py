# Generated by Django 5.0.2 on 2024-03-03 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanager', '0005_distribute_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribute',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distribute', to='assetmanager.asset'),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distribute', to='assetmanager.employee'),
        ),
    ]
