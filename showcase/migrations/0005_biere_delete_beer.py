# Generated by Django 5.1 on 2025-02-11 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0004_evenement_afficher_lien'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=100)),
                ('degre', models.DecimalField(decimal_places=1, max_digits=3, verbose_name="Degré d'alcool")),
                ('volume', models.IntegerField(help_text='Volume en cl')),
                ('est_disponible', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='bieres/')),
                ('ordre_affichage', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Bière',
                'verbose_name_plural': 'Bières',
                'ordering': ['ordre_affichage'],
            },
        ),
        migrations.DeleteModel(
            name='Beer',
        ),
    ]
