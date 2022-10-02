# Generated by Django 4.1 on 2022-10-01 22:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0013_remove_coupon_valid_to_alter_coupon_valid_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='valid_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
