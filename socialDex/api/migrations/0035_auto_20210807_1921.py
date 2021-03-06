# Generated by Django 3.2.5 on 2021-08-07 17:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20210807_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expiringTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 19, 21, 36, 329756)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='viewStart',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 19, 21, 36, 329756)),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='timeToNextUpdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 19, 21, 36, 329756, tzinfo=utc)),
        ),
    ]
