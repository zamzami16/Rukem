# Generated by Django 4.2.3 on 2023-07-22 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nominal', models.FloatField(default=0, verbose_name='nominal')),
                ('keterangan', models.TextField(verbose_name='Keterangan')),
                ('tanggal', models.DateTimeField(auto_now_add=True, verbose_name='tanggal input')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
