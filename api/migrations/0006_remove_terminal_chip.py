# Generated by Django 4.1.5 on 2023-01-23 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_chip_terminal_chip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terminal',
            name='chip',
        ),
    ]
