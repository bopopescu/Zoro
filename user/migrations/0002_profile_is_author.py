# Generated by Django 2.2.9 on 2020-02-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
    ]
