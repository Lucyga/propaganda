# Generated by Django 3.1.4 on 2020-12-17 23:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_remove_libri_copertina'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generi',
            options={'verbose_name': 'Generi', 'verbose_name_plural': 'Generi'},
        ),
        migrations.AddField(
            model_name='libri',
            name='data_caricamento',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]