# Generated by Django 3.0.6 on 2020-07-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adapp", "0007_auto_20200717_1408"),
    ]

    operations = [
        migrations.RemoveField(model_name="ad", name="tags",),
        migrations.AddField(
            model_name="ad",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags", to="adapp.Tag", verbose_name="Теги"
            ),
        ),
    ]
