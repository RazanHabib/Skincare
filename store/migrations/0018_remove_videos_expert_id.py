# Generated by Django 5.0 on 2024-03-17 11:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0017_alter_experts_user_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="videos",
            name="expert_id",
        ),
    ]
