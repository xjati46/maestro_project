# Generated by Django 3.0.7 on 2020-07-13 04:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0007_auto_20200713_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='rapor',
            name='gaya_bebas_1',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Teknik Kaki dan Pengambilan Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_bebas_2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Teknik Tangan dan Pengambilan Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_bebas_3',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Koordinasi Kaki, Tangan, Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_dada_1',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Teknik Kaki dan Pengambilan Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_dada_2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Teknik Tangan dan Pengambilan Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_dada_3',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Koordinasi Kaki, Tangan, Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_kupu_1',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Teknik Kaki dan Pengambilan Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_kupu_2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Teknik Tangan dan Pengambilan Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_kupu_3',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Koordinasi Kaki, Tangan, Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_punggung_1',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Teknik Kaki dan Pengambilan Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_punggung_2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Teknik Tangan dan Pengambilan Nafas'),
        ),
        migrations.AddField(
            model_name='rapor',
            name='gaya_punggung_3',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Koordinasi Kaki, Tangan, Nafas'),
        ),
    ]
