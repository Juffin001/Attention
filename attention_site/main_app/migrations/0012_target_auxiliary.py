# Generated by Django 4.2.3 on 2023-08-13 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_target_important_alter_target_day_to_beat'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='auxiliary',
            field=models.BooleanField(default=0),
        ),
    ]
