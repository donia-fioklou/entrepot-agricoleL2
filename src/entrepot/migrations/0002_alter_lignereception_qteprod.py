# Generated by Django 4.0.5 on 2022-08-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrepot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lignereception',
            name='qteProd',
            field=models.PositiveIntegerField(),
        ),
    ]
