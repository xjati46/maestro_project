# Generated by Django 3.0.7 on 2020-07-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_auto_20200712_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='p1_a',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
