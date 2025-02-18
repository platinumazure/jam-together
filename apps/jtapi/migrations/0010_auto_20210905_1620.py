# Generated by Django 3.2.5 on 2021-09-05 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jtapi', '0009_auto_20210905_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songpart',
            old_name='full_file_url',
            new_name='part_file_url',
        ),
        migrations.CreateModel(
            name='SongPartPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_file_url', models.URLField()),
                ('song_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='jtapi.songpart')),
            ],
            options={
                'order_with_respect_to': 'song_part',
            },
        ),
    ]
