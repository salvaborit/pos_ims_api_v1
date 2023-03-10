# Generated by Django 4.1.5 on 2023-01-16 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('connectivity', models.CharField(choices=[('full', 'full'), ('3g', '3g'), ('3g-wifi', '3g-wifi'), ('eth', 'eth')], max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=255, unique=True)),
                ('part_number', models.CharField(max_length=255)),
                ('id_pos2000', models.CharField(max_length=8, unique=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.client')),
                ('location', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.location')),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.model')),
            ],
        ),
    ]
