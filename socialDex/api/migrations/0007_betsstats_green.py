# Generated by Django 3.2.5 on 2021-07-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_betsstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='betsstats',
            name='green',
            field=models.BooleanField(default=False),
        ),
    ]