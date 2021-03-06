# Generated by Django 3.2.5 on 2021-07-26 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_betsstats_green'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isBetting',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='OpenBids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=30)),
                ('bidAmount', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'OPEN'), (1, 'WIN'), (-1, 'LOSS')], default=0)),
                ('returns', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
