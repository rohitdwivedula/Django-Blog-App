# Generated by Django 2.0.9 on 2019-01-11 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190103_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.TextField()),
                ('text', models.TextField()),
                ('published_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
