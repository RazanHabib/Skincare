# Generated by Django 5.0 on 2024-03-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0010_alter_orders_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="governate",
            field=models.TextField(blank=True, null=True),
        ),
    ]
