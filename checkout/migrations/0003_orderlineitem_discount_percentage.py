# Generated by Django 3.0.8 on 2020-08-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200803_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='discount_percentage',
            field=models.IntegerField(default=0),
        ),
    ]
