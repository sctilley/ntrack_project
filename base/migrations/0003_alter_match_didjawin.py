# Generated by Django 4.2.7 on 2023-11-18 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_league_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='didjawin',
            field=models.BooleanField(default=None, null=True, verbose_name='Match Win'),
        ),
    ]
