# Generated by Django 2.2.9 on 2019-12-26 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0020_delete_collection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isbn',
            new_name='isbn13',
        ),
    ]
