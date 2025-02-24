# Generated by Django 5.0 on 2024-03-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0019_videos_expert_id_alter_experts_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experts",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="products",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="videos",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="videos",
            name="link",
            field=models.FileField(upload_to="videos/"),
        ),
    ]
