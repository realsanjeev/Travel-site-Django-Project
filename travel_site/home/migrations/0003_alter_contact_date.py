# Generated by Django 4.2.2 on 2023-06-23 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 6, 23, 5, 36, 7, 470201, tzinfo=datetime.timezone.utc)),
        ),
    ]