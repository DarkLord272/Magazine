# Generated by Django 4.1.4 on 2022-12-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hot',
            field=models.BooleanField(default=False),
        ),
    ]
