# Generated by Django 3.2.5 on 2021-07-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]