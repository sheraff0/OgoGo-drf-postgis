# Generated by Django 4.2.2 on 2023-06-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='website',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
