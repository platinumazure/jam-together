from rest_framework_json_api.views import ModelViewSet, ReadOnlyModelViewSet, RelationshipView
from django.contrib.auth.models import User
from ..models import SongProvider, Song, JamSessionSong
from ..permissions import IsConductorOrAdminOrReadOnly, IsAdminOrReadOnly
from ..serializers import (
    SongProviderSerializer,
    SongSerializer,
    JamSessionSongSerializer,
    UserSerializer,
)

from .jam_session_views import *
from .song_part_views import *

class SongProviderViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = SongProvider.objects.all()
    serializer_class = SongProviderSerializer


class SongViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class JamSessionSongViewSet(ModelViewSet):
    permission_classes = (IsConductorOrAdminOrReadOnly,)
    queryset = JamSessionSong.objects.all()
    serializer_class = JamSessionSongSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Relationship views

class SongRelationshipView(RelationshipView):
    queryset = Song.objects.all()


class JamSessionSongRelationshipView(RelationshipView):
    queryset = JamSessionSong.objects.all()
