# Generated by Django 4.2.9 on 2024-01-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
