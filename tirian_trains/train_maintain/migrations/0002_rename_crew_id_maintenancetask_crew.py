# Generated by Django 4.2.7 on 2023-11-30 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train_maintain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintenancetask',
            old_name='crew_ID',
            new_name='crew',
        ),
    ]
