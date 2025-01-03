# Generated by Django 4.2.7 on 2024-11-12 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gm', '0004_workout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exerc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sets', models.IntegerField()),
                ('reps', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='exercises/')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises_set', to='gm.workout')),
            ],
        ),
    ]
