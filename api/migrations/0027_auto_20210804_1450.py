# Generated by Django 3.2.5 on 2021-08-04 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20210804_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expiringTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 14, 50, 19, 55608)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='viewStart',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 14, 50, 19, 55608)),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='timeToNextUpdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 14, 50, 19, 55608)),
        ),
    ]
