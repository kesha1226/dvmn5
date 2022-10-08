# Generated by Django 4.1.2 on 2022-10-08 17:06

from django.db import migrations
from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps


def create_owners(apps: StateApps, schema_editor: DatabaseSchemaEditor):
    flat_model = apps.get_model("property", "Flat")
    owner_model = apps.get_model("property", "Owner")
    for flat in flat_model.objects.all():
        owner_model.objects.get_or_create(
            fio=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            defaults={
                "owner_pure_phone": flat.owner_pure_phone,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0011_owner"),
    ]

    operations = [migrations.RunPython(create_owners)]
