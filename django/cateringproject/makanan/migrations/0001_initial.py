# Generated by Django 4.1.3 on 2022-12-04 07:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catering',
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
                ('gambar', models.ImageField(upload_to='makanan/images/')),
                ('stok', models.IntegerField()),
                ('tersedia', models.CharField(choices=[('1', 'Tersedia'), ('2', 'Tidak tersedia')], max_length=1)),
                ('Catering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makanan.catering')),
            ],
        ),
    ]