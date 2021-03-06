# Generated by Django 3.1 on 2020-08-16 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20200816_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.auction'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.auction'),
        ),
    ]
