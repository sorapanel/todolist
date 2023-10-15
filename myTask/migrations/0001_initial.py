# Generated by Django 4.2.1 on 2023-10-15 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('task_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('finish_date', models.DateField()),
                ('finish_time', models.TimeField()),
                ('like', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
