# Generated by Django 4.1.2 on 2022-10-08 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0015_auto_20221008_2118"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="flat",
            name="owner",
        ),
        migrations.RemoveField(
            model_name="flat",
            name="owner_pure_phone",
        ),
        migrations.RemoveField(
            model_name="flat",
            name="owners_phonenumber",
        ),
    ]
