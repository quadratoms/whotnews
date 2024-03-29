# Generated by Django 3.1.3 on 2020-11-23 00:59

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cartegory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(choices=[('Religion', 'Religion'), ('Culture', 'Culture'), ('Education', 'Education'), ('Fashion', 'Fashion'), ('Technology', 'Technology'), ('Art&music', 'Art&Music'), ('Cooking', 'Cooking'), ('Entertainment', 'Entertainment'), ('Garden', 'Garden'), ('Health&Fittness', 'Health&Fittness'), ('History', 'History'), ('Kid', 'Kid'), ('Medical', 'Medical'), ('Parenting', 'Parenting'), ('Romance', 'Romance'), ('Sport', 'Sport')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.DateField(blank=True, null=True)),
                ('profession', models.CharField(max_length=10, null=True)),
                ('telephone', models.IntegerField(blank=True, default='0', null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('about', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article_img', models.ImageField(blank=True, upload_to='article_image')),
                ('article_body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('view', models.IntegerField(default=0)),
                ('article_cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newblog.cartegory')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
