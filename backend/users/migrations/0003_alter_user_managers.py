# Generated by Django 4.1.3 on 2023-06-03 08:58

from django.db import migrations

import users.models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_avatar_alter_user_email_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", users.models.CustomUserManager()),
            ],
        ),
    ]
