# Generated by Django 4.2.7 on 2023-11-30 08:14

from django.db import migrations, models
import django.db.models.deletion
import train_maintain.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaintainanceCrew',
            fields=[
                ('crew_ID', models.AutoField(primary_key=True, serialize=False)),
                ('crew_leader', models.CharField(max_length=60)),
                ('specialty_skill', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_ID', models.AutoField(primary_key=True, serialize=False)),
                ('train_model', models.CharField(max_length=15, validators=[train_maintain.models.validate_custom_format])),
                ('max_speed', models.IntegerField()),
                ('no_of_seats', models.IntegerField()),
                ('no_of_toilets', models.IntegerField()),
                ('bool_reclining_seats', models.BooleanField()),
                ('bool_folding_tables', models.BooleanField()),
                ('bool_disability_access', models.BooleanField()),
                ('bool_luggage_storage', models.BooleanField()),
                ('bool_vending_machine', models.BooleanField()),
                ('bool_food_service', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceTask',
            fields=[
                ('maintenance_task_ID', models.AutoField(primary_key=True, serialize=False)),
                ('date_maintained', models.DateField()),
                ('condition', models.CharField(max_length=50)),
                ('maintenance_description', models.TextField(max_length=255)),
                ('crew_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_maintain.maintainancecrew')),
            ],
        ),
    ]
