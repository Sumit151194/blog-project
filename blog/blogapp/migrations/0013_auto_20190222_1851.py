# Generated by Django 2.1.7 on 2019-02-22 13:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0012_auto_20190222_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_rdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 13, 21, 1, 217515, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 13, 21, 1, 238988, tzinfo=utc)),
        ),
    ]