# Generated by Django 5.1.6 on 2025-02-20 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_anexo_id_leiloeiro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anexo',
            name='id_leiloeiro',
        ),
    ]
