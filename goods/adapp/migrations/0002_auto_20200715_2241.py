# Generated by Django 3.0.6 on 2020-07-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/', verbose_name='Фотография'),
        ),
    ]