# Generated by Django 4.2.3 on 2023-08-13 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_target_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
