# Generated by Django 5.1.5 on 2025-03-12 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_budgettable_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalstablecreation',
            name='amount_now',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='goalstablecreation',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
