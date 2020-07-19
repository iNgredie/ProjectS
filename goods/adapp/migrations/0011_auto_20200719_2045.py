# Generated by Django 3.0.6 on 2020-07-19 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adapp', '0010_auto_20200719_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='tags',
        ),
        migrations.AddField(
            model_name='ad',
            name='tag',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='adapp.Tag'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фотография'),
        ),
    ]