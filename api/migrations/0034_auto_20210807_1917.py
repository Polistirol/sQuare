# Generated by Django 3.2.5 on 2021-08-07 17:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_auto_20210807_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expiringTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 19, 17, 42, 568592)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='viewStart',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 19, 17, 42, 568592)),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='timeToNextUpdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 19, 17, 42, 567595, tzinfo=utc)),
        ),
    ]
