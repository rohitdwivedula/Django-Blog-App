# Generated by Django 2.0.9 on 2019-01-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='message_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
