# Generated by Django 2.2.9 on 2019-12-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0022_auto_20191226_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='end_date',
            field=models.DateField(default='2019-12-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='start_date',
            field=models.DateField(default='2019-05-23'),
            preserve_default=False,
        ),
    ]
