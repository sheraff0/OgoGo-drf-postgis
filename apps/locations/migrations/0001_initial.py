# Generated by Django 4.2.2 on 2023-06-12 12:33

import contrib.utils.date_time
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Last update time')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
                ('coords', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('time_zone', models.CharField(default='Europe/Moscow', max_length=32, validators=[contrib.utils.date_time.validate_timezone], verbose_name='Часовой пояс')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
    ]
