# Generated by Django 4.2.2 on 2023-06-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='price',
        ),
        migrations.AddField(
            model_name='offer',
            name='grade',
            field=models.IntegerField(blank=True, null=True, verbose_name='Уровень крутости'),
        ),
        migrations.AddField(
            model_name='offer',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]
