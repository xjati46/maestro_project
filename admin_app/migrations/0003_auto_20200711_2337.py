# Generated by Django 3.0.7 on 2020-07-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_auto_20200711_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='diskon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
