# Generated by Django 4.1.2 on 2022-11-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_is_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.TextField(default=0),
        ),
    ]