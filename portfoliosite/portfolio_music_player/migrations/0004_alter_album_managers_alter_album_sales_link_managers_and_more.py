# Generated by Django 4.0.4 on 2022-07-25 17:12

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_music_player', '0003_alter_album_description_alter_song_description'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='album',
            managers=[
                ('albums', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='album_sales_link',
            managers=[
                ('album_sales_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='song',
            managers=[
                ('songs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='track_number',
            managers=[
                ('track_numbers', django.db.models.manager.Manager()),
            ],
        ),
    ]
