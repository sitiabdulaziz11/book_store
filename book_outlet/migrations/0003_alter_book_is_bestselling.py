# Generated by Django 4.2.17 on 2025-03-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_book_author_book_is_bestselling_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_bestselling',
            field=models.BooleanField(default=True),
        ),
    ]
