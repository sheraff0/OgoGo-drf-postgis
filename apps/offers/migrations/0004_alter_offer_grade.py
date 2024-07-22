# Generated by Django 4.2.2 on 2023-07-03 05:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_calendar_only_weekdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='grade',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Уровень крутости'),
        ),
    ]
