# Generated by Django 4.0.5 on 2022-07-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrepot', '0015_ligneconteneur_expedition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='qteActu',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zone',
            name='qteMax',
            field=models.PositiveIntegerField(),
        ),
    ]
