# Generated by Django 4.2.2 on 2024-01-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesHub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('rq_id', models.AutoField(primary_key=True, serialize=False)),
                ('request_name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
