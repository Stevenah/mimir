# Generated by Django 2.1.2 on 2018-10-14 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='source',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='class_index',
        ),
        migrations.RemoveField(
            model_name='image',
            name='class_label',
        ),
        migrations.RemoveField(
            model_name='image',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='prediction',
        ),
    ]
