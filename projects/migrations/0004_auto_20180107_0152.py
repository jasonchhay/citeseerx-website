# Generated by Django 2.0 on 2018-01-07 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20180107_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]
