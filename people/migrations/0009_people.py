# Generated by Django 2.0 on 2017-12-26 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20171226_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('webpageurl', models.CharField(max_length=200)),
                ('shortdescription', models.CharField(max_length=200)),
                ('image', models.ImageField(default='noimage.png', upload_to='people_portraits/')),
                ('occupation', models.CharField(choices=[('Postdocs', 'Postdocs'), ('PhD Students', 'PhD Students'), ('Masters Students', 'Masters Students'), ('Undergraduates', 'Undergraduates'), ('Staff', 'Staff')], default='Postdoc', max_length=25)),
                ('alumni', models.BooleanField(default=False)),
            ],
        ),
    ]
