# Generated by Django 2.2.9 on 2020-02-06 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20200206_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='chapters',
        ),
        migrations.AddField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chapter_book', to='book.Book'),
            preserve_default=False,
        ),
    ]
