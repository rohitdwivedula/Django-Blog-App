# Generated by Django 2.0.9 on 2019-01-03 04:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181227_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 3, 4, 21, 44, 286862, tzinfo=utc)),
        ),
    ]
