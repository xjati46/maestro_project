# Generated by Django 3.0.7 on 2020-07-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach_app', '0004_auto_20200715_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='bagi_hasil',
            field=models.FloatField(blank=True, default=0.5, null=True),
        ),
    ]
