# Generated by Django 3.2.2 on 2021-06-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
