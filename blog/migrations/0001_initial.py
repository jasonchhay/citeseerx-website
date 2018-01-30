# Generated by Django 2.0 on 2018-01-07 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2018, 1, 7, 19, 38, 3, 920430))),
                ('blogtitle', models.CharField(max_length=200)),
                ('postername', models.CharField(blank=True, max_length=1000, null=True)),
                ('link', models.CharField(blank=True, max_length=1000)),
                ('description', models.TextField(max_length=10000)),
            ],
        ),
    ]
