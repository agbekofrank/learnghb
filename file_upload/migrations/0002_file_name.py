# Generated by Django 2.2.12 on 2020-05-13 22:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(default=datetime.datetime(2020, 5, 13, 22, 22, 9, 236987, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]
