# Generated by Django 4.2.9 on 2024-01-23 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_product_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='aut',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='cat',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='name',
            new_name='ty',
        ),
    ]
