# Generated by Django 4.2.9 on 2024-01-22 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
