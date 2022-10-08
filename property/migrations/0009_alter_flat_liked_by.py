# Generated by Django 4.1.2 on 2022-10-08 14:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("property", "0008_flat_owner_pure_phone_alter_flat_has_balcony"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flat",
            name="liked_by",
            field=models.ManyToManyField(
                blank=True,
                related_name="liked_posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Кто лайкнул:",
            ),
        ),
    ]
