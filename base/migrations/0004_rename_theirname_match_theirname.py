# Generated by Django 4.2.7 on 2023-11-18 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_match_didjawin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='theirname',
            new_name='theirName',
        ),
    ]
