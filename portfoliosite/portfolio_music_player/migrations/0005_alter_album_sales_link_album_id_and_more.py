# Generated by Django 4.0.4 on 2024-07-09 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_music_player', '0004_alter_album_managers_alter_album_sales_link_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album_sales_link',
            name='album_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_links', to='portfolio_music_player.album'),
        ),
        migrations.AlterField(
            model_name='song_file',
            name='song_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_files', to='portfolio_music_player.song'),
        ),
        migrations.AlterField(
            model_name='track_number',
            name='album_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='portfolio_music_player.album'),
        ),
        migrations.AlterField(
            model_name='track_number',
            name='song_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_nums', to='portfolio_music_player.song'),
        ),
    ]
