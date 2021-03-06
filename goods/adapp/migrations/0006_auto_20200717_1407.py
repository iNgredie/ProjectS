# Generated by Django 3.0.6 on 2020-07-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adapp", "0005_auto_20200716_2227"),
    ]

    operations = [
        migrations.RenameField(model_name="tag", old_name="title", new_name="name",),
        migrations.AlterField(
            model_name="ad",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags", to="adapp.Tag", verbose_name="Теги"
            ),
        ),
    ]
