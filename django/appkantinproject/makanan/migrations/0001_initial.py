# Generated by Django 4.1.3 on 2022-12-02 08:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kantin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('telpon', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='min 8 digit', regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Makanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('harga', models.IntegerField()),
                ('gambar', models.ImageField(upload_to='movies/images/')),
                ('stok', models.IntegerField()),
                ('tersedia', models.CharField(choices=[('1', 'Tersedia'), ('0', 'Tidak Tersedia')], max_length=1)),
                ('Kantin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makanan.kantin')),
            ],
        ),
    ]
