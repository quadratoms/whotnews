# Generated by Django 4.2 on 2023-04-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_cartegory_id_alter_comment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='author',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
