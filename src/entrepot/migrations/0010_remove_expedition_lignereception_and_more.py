# Generated by Django 4.0.5 on 2022-07-25 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrepot', '0009_alter_expedition_qte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expedition',
            name='ligneReception',
        ),
        migrations.AddField(
            model_name='lignereception',
            name='expedition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entrepot.expedition'),
        ),
    ]
