# Generated by Django 3.0.8 on 2020-07-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0007_auto_20200714_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='p1_a',
            field=models.BooleanField(),
        ),
    ]