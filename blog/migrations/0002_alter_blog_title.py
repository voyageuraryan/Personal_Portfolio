# Generated by Django 4.2.6 on 2023-10-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=500),
        ),
    ]
