# Generated by Django 3.0.8 on 2020-08-15 09:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_orderlineitem_discount_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(models.DecimalField(decimal_places=2, editable=False, max_digits=6))]),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
