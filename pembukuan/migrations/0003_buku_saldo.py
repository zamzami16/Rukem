# Generated by Django 4.2.3 on 2023-07-22 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan', '0002_buku_jenis'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='saldo',
            field=models.FloatField(default=0, verbose_name='saldo'),
        ),
    ]
