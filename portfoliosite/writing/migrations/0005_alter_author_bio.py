# Generated by Django 5.0.7 on 2024-07-10 19:58

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0004_alter_writing_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]