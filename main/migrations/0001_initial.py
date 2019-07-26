# Generated by Django 2.2.2 on 2019-07-23 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=200)),
                ('review_content', models.TextField()),
                ('review_published', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]
