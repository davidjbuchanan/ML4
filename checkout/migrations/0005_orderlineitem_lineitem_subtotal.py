# Generated by Django 3.0.8 on 2020-08-16 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20200815_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='lineitem_subtotal',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6),
        ),
    ]
