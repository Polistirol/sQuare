# Generated by Django 3.2.5 on 2021-08-04 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210804_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expiringTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 11, 32, 27, 331282)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='viewStart',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 11, 32, 27, 331282)),
        ),
    ]
