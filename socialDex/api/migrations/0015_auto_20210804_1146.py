# Generated by Django 3.2.5 on 2021-08-04 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210804_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expiringTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 4, 11, 46, 42, 839071)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='viewStart',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 11, 46, 42, 839071)),
        ),
    ]