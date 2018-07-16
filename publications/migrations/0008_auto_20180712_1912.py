# Generated by Django 2.0.6 on 2018-07-12 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0007_auto_20180710_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='bibfile',
        ),
        migrations.AddField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Journal', 'Journal Papers'), ('Conference', 'Conference Papers')], default='Journal', max_length=25),
        ),
        migrations.AlterField(
            model_name='publication',
            name='venue',
            field=models.CharField(max_length=200),
        ),
    ]