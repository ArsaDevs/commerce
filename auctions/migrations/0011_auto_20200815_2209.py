# Generated by Django 3.1 on 2020-08-15 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auction_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='status',
            new_name='active',
        ),
    ]