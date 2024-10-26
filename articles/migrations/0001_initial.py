# Generated by Django 5.1.2 on 2024-10-23 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('views', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('date', models.DateField(default=datetime.datetime(2024, 10, 23, 19, 58, 7, 548369), verbose_name='Date')),
            ],
        ),
    ]
