# Generated by Django 3.0.2 on 2020-04-18 17:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20200418_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='time_ending',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 17, 23, 40, 842588, tzinfo=utc)),
        ),
    ]
