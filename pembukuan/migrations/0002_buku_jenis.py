# Generated by Django 4.2.3 on 2023-07-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='jenis',
            field=models.SmallIntegerField(choices=[(1, 'Pemasukan'), (-1, 'Pengeluaran')], default=1),
        ),
    ]