# Generated by Django 4.1.7 on 2023-03-16 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_homeads_delete_onsalehouse_delete_rentalhouse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeads',
            name='title_deed',
        ),
    ]