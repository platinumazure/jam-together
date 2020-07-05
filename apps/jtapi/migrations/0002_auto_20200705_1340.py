# Generated by Django 3.0.7 on 2020-07-05 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jtapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JamSessionMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jam_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jtapi.JamSession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jamsession',
            name='members',
            field=models.ManyToManyField(related_name='jam_session_memberships', through='jtapi.JamSessionMembership', to=settings.AUTH_USER_MODEL),
        ),
    ]
