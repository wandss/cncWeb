# Generated by Django 2.1.7 on 2019-03-25 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
        ('rpi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='used_pins',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together={('device', 'used_pins')},
        ),
    ]
