# Generated by Django 4.2 on 2023-04-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_newsmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='heading',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
