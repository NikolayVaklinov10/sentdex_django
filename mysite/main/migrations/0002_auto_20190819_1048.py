# Generated by Django 2.2.1 on 2019-08-19 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 19, 10, 48, 39, 507872), verbose_name='date published'),
        ),
    ]
