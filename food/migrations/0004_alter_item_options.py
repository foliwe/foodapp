# Generated by Django 4.2.7 on 2023-11-23 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_created_at_item_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-created_at']},
        ),
    ]