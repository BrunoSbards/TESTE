# Generated by Django 5.1.6 on 2025-02-20 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_anexo_id_leiloeiro'),
    ]

    operations = [
        migrations.AddField(
            model_name='anexo',
            name='id_leiloeiro',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.leiloeiro'),
        ),
    ]
