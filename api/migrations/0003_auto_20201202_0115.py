# Generated by Django 3.1.3 on 2020-12-02 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201202_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinginfo',
            name='creditcard_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='billinginfo',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]
