# Generated by Django 4.1.2 on 2022-10-08 14:29

from django.db import migrations
from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps

import phonenumbers


def validate_phones(apps: StateApps, schema_editor: DatabaseSchemaEditor):
    flat_model = apps.get_model("property", "Flat")
    for flat in flat_model.objects.all():
        parsed_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        phone = f"+7{parsed_phone.national_number}"
        if not phonenumbers.is_valid_number(parsed_phone):
            phone = ""
        flat.owner_pure_phone = phone
        flat.save()


def move_backward(apps, schema_editor):
    flat_model = apps.get_model("property", "Flat")
    for flat in flat_model.objects.all():
        flat.owner_pure_phone = ""
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0009_alter_flat_liked_by"),
    ]

    operations = [migrations.RunPython(validate_phones, move_backward)]