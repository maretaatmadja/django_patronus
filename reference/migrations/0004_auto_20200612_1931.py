# Generated by Django 3.0.7 on 2020-06-12 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_auto_20200612_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reference',
            options={'ordering': ('-created',)},
        ),
    ]
