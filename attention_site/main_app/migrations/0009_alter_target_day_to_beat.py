# Generated by Django 4.2.3 on 2023-08-10 01:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_target_time_to_beat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='day_to_beat',
            field=models.DateField(default=datetime.date.today, verbose_name='on what day need to be maden?'),
        ),
    ]
