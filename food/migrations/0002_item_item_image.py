# Generated by Django 4.2.7 on 2023-11-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://placehold.co/600x400.png', max_length=500),
        ),
    ]