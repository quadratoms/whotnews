# Generated by Django 3.1.2 on 2020-11-22 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201113_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='newscat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.cartegory'),
        ),
    ]
