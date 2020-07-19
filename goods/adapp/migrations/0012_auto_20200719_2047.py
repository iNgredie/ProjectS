# Generated by Django 3.0.6 on 2020-07-19 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adapp', '0011_auto_20200719_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='adapp.Tag'),
        ),
    ]
