# Generated by Django 2.1.7 on 2019-03-23 17:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('motor', '0001_initial'),
        ('rpi', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gcode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gcode_file', models.FileField(upload_to='media')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motor', models.ManyToManyField(to='motor.Motor')),
                ('pi_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpi.RpiBoard')),
            ],
        ),
    ]
