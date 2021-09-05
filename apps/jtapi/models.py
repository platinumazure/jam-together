from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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

    def __str__(self):
        return self.name


class JamSessionMembership(models.Model):
    jam_session = models.ForeignKey(JamSession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} in {self.jam_session}'


class SongProvider(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    site_url = models.URLField()

    # TODO: Add fields for URL patterns for retrieving song info?

    def __str__(self):
        return f'{self.name} ({self.site_url})'


class Song(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    artist = models.CharField(max_length=200, blank=True)
    composer = models.CharField(max_length=200, blank=True)
    arranger = models.CharField(max_length=200, blank=True)

    song_provider = models.ForeignKey(
        SongProvider,
        on_delete=models.CASCADE,
        related_name = 'songs',
    )

    def __str__(self):
        if self.subtitle:
            full_title = f'{self.title} ({self.subtitle})'
        else:
            full_title = self.title

        return f'{full_title} ({self.song_provider.name})'


class PartDefinition(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class PartTypes(models.TextChoices):
        INSTRUMENT = 'Instrument'
        TRANSPOSITION = 'Transposition'

    part_type = models.CharField(max_length=20, choices=PartTypes.choices)

    def __str__(self):
        return f'{self.name} ({self.part_type})'


class SongPart(models.Model):
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name='parts',
    )
    definition = models.ForeignKey(
        PartDefinition,
        on_delete=models.PROTECT,
        related_name='+',
    )

    number = models.PositiveSmallIntegerField(null=True, blank=True)

    reference_url = models.URLField(blank=True)
    part_file_url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.song} ({self.definition.name})'


class SongPartPage(models.Model):
    song_part = models.ForeignKey(
        SongPart,
        on_delete=models.CASCADE,
        related_name='pages',
    )
    page_file_url = models.URLField()

    class Meta:
        order_with_respect_to = 'song_part'
