# Generated by Django 3.0.7 on 2020-07-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_rapor_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapor',
            name='waktu_post',
            field=models.DateField(auto_now_add=True),
        ),
    ]
