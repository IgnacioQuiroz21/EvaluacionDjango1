# Generated by Django 3.2.2 on 2021-06-14 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProv', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Proveedor')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Parche',
            fields=[
                ('idParche', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaParche', models.DateField(verbose_name='Fecha del Parche')),
                ('descParche', models.CharField(max_length=200, verbose_name='Descripcion del Parche')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='combate.proveedor', verbose_name='Nombre del Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('idAnuncio', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descAnuncio', models.CharField(max_length=200, verbose_name='Descripcion del Parche')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='combate.proveedor', verbose_name='Nombre Del Proveedor')),
            ],
        ),
    ]
