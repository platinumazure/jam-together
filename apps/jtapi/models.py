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
