# Generated by Django 3.1.4 on 2020-12-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_auto_20201218_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='libri',
            name='disponibile',
            field=models.BooleanField(default=True),
        ),
    ]
