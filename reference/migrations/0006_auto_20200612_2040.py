# Generated by Django 3.0.7 on 2020-06-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0005_reference_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='slug',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]