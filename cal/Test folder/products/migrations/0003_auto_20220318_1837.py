# Generated by Django 2.2.12 on 2022-03-18 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offering'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offering',
            new_name='Offer',
        ),
    ]
