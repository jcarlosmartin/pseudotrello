# Generated by Django 3.1.3 on 2020-12-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201204_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='projects',
            field=models.ManyToManyField(null=True, to='api.Project'),
        ),
    ]
