# Generated by Django 3.1.1 on 2020-09-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalcontribution',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
