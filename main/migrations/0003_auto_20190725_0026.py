# Generated by Django 2.1.4 on 2019-07-25 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190722_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_genre',
            field=models.CharField(default=8, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='review_rating',
            field=models.PositiveSmallIntegerField(default=8),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 25, 0, 26, 0, 877066), verbose_name='Date Published'),
        ),
    ]