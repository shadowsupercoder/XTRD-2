# Generated by Django 2.1 on 2018-08-30 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_etherdelta'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EtherDelta',
            new_name='Coinsuper',
        ),
        migrations.RenameModel(
            old_name='Etherscan',
            new_name='TokenJar',
        ),
    ]