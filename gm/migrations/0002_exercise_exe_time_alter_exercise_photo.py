# Generated by Django 5.1 on 2024-08-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='Exe_time',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='photo',
            field=models.ImageField(upload_to='r'),
        ),
    ]