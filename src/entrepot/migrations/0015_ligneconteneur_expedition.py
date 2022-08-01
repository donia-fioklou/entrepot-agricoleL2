# Generated by Django 4.0.5 on 2022-07-27 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrepot', '0014_remove_lignereception_expedition'),
    ]

    operations = [
        migrations.AddField(
            model_name='ligneconteneur',
            name='expedition',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='entrepot.expedition'),
            preserve_default=False,
        ),
    ]