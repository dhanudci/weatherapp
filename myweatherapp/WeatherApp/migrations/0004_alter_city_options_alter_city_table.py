# Generated by Django 4.1.4 on 2022-12-16 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("WeatherApp", "0003_alter_city_options_alter_city_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={},
        ),
        migrations.AlterModelTable(
            name="city",
            table="city",
        ),
    ]
