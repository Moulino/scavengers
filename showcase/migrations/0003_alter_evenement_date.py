# Generated by Django 5.1 on 2025-02-11 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_evenement_delete_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='date',
            field=models.DateField(),
        ),
    ]
