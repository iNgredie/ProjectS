# Generated by Django 3.0.6 on 2020-07-19 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adapp", "0008_auto_20200717_1514"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ad", old_name="views", new_name="view_count",
        ),
    ]
