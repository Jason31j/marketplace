# Generated by Django 4.2.1 on 2023-10-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_product_price_alter_product_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=120, null=True),
        ),
    ]
