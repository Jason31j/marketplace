# Generated by Django 4.2.1 on 2023-10-19 00:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0003_review_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="slug",
        ),
    ]
