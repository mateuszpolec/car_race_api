# Generated by Django 3.1.2 on 2020-10-09 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_race_api', '0009_auto_20201009_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='x_position',
            new_name='time_map1',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='y_position',
            new_name='time_map2',
        ),
    ]