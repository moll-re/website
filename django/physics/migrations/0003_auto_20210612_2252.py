# Generated by Django 2.1.15 on 2021-06-12 22:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0002_auto_20210612_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 12, 22, 52, 14, 426795, tzinfo=utc), verbose_name='Date published'),
        ),
    ]