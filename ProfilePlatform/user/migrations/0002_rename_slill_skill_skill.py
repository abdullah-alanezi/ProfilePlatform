# Generated by Django 5.0.1 on 2024-02-03 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='slill',
            new_name='skill',
        ),
    ]