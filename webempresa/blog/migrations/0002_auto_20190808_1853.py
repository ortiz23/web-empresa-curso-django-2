# Generated by Django 2.0.2 on 2019-08-08 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 18, 53, 4, 578910, tzinfo=utc), verbose_name='Fecha de creación'),
        ),
    ]
