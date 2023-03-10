# Generated by Django 4.1.5 on 2023-01-26 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_rename_acquirer_id_terminal_acquirer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connectivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=31, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='terminal',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='acquirer',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='connectivity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.connectivity'),
        ),
    ]
