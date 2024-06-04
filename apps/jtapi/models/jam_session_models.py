from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from .song_models import Song

# Import the current User model
User = get_user_model()

class JamSession(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    conductor = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    is_unlisted = models.BooleanField(default=False)

    members = models.ManyToManyField(
        User,
        related_name='jam_session_memberships',
        through='JamSessionMembership'
    )

    created_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)

    @property
    def current_song(self):
        return self.songs.filter(state=JamSessionSong.JamSessionSongStates.QUEUED).first()

    @property
    def queued_songs(self):
        return self.songs.filter(state=JamSessionSong.JamSessionSongStates.QUEUED).order_by('date_queued')

    def __str__(self):
        return self.name


class JamSessionMembership(models.Model):
    jam_session = models.ForeignKey(JamSession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} in {self.jam_session}'


class JamSessionSong(models.Model):
    jam_session = models.ForeignKey(
        JamSession,
        related_name='songs',
        on_delete=models.CASCADE,
    )

    song = models.ForeignKey(
        Song,
        related_name='+',
        on_delete=models.CASCADE,
    )

    date_queued = models.DateTimeField(default=timezone.now)
    date_played = models.DateTimeField(null=True, blank=True)

    class JamSessionSongStates(models.TextChoices):
        QUEUED = 'Queued'
        CANCELED = 'Canceled'
        DEFERRED = 'Deferred'
        PLAYED = 'Played'

    state = models.CharField(
        max_length=10,
        choices=JamSessionSongStates.choices,
        default=JamSessionSongStates.QUEUED,
    )

    def save(self, *args, **kwargs):
        if self.state == JamSessionSong.JamSessionSongStates.PLAYED and self.date_played is None:
            self.date_played = timezone.now()
        elif self.state != JamSessionSong.JamSessionSongStates.PLAYED and self.date_played is not None:
            self.date_played = None

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.song.title} ({self.state} in "{self.jam_session.name}")'
