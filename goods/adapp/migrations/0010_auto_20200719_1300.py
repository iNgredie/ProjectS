# Generated by Django 3.0.6 on 2020-07-19 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adapp', '0009_auto_20200719_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='tags',
        ),
        migrations.AddField(
            model_name='ad',
            name='tags',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='adapp.Tag'),
        ),
    ]
