# Generated by Django 5.0.4 on 2024-05-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buses',
            name='bus_no',
            field=models.IntegerField(),
        ),
    ]
