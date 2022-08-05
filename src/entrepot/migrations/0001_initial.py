# Generated by Django 4.0.5 on 2022-08-03 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('immatriculation', models.CharField(max_length=100)),
                ('dateCreation', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Bateau',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('dateCreation', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('adresse', models.CharField(max_length=200)),
                ('dateCreation', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Conteneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdProprietaire', models.CharField(max_length=4, null=True)),
                ('numCon', models.PositiveIntegerField(max_length=6, null=True)),
                ('typeCon', models.CharField(max_length=4, null=True)),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('bateau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entrepot.bateau')),
            ],
            options={
                'verbose_name': 'Conteneur',
            },
        ),
        migrations.CreateModel(
            name='Entrepot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('dateCreation', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Entrepot',
            },
        ),
        migrations.CreateModel(
            name='Expedition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomExp', models.CharField(blank=True, max_length=50, unique=True)),
                ('dateExp', models.DateField()),
                ('qte', models.IntegerField(blank=True, null=True)),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entrepot.client')),
                ('conteneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.conteneur')),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('adresse', models.CharField(max_length=200)),
                ('dateCreation', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProd', models.CharField(max_length=50)),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.categorie')),
            ],
            options={
                'verbose_name': 'Produit',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('qteMax', models.PositiveIntegerField()),
                ('qteActu', models.PositiveIntegerField(blank=True, null=True)),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('entrepot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.entrepot')),
            ],
            options={
                'verbose_name': 'Zone',
            },
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomRecep', models.CharField(max_length=30)),
                ('dateRecep', models.DateField()),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.fournisseur')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.produit')),
            ],
        ),
        migrations.CreateModel(
            name='LigneReception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qteProd', models.IntegerField()),
                ('numLot', models.CharField(max_length=100)),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('expedier', models.BooleanField(default=False)),
                ('reception', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.reception')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.zone')),
            ],
        ),
        migrations.CreateModel(
            name='LigneConteneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.conteneur')),
                ('expedition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.expedition')),
                ('ligneReception', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepot.lignereception')),
            ],
        ),
    ]
