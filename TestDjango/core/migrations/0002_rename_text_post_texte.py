# Generated by Django 4.1.5 on 2023-01-21 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='texte',
        ),
    ]
