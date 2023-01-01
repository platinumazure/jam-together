from rest_framework.permissions import IsAdminUser
from rest_framework_json_api.views import ModelViewSet, ReadOnlyModelViewSet, RelationshipView
from django.contrib.auth.models import User
from django.db.models import Q
from .models import (
    JamSession, SongProvider, Song, JamSessionSong, PartDefinition, SongPart,
    SongPartPage,
)
from .permissions import IsConductorOrAdminOrReadOnly, IsAdminOrReadOnly
from .serializers import (
    JamSessionSerializer,
    PartDefinitionSerializer,
    SongProviderSerializer,
    SongSerializer,
    JamSessionSongSerializer,
    SongPartSerializer,
    SongPartPageSerializer,
    UserSerializer,
)

class JamSessionViewSet(ModelViewSet):
    permission_classes = (IsConductorOrAdminOrReadOnly,)
    queryset = JamSession.objects.all()
    serializer_class = JamSessionSerializer

    def get_queryset(self):
        """Retrieve jam sessions user can view.

        Non-admins can view:
        - Jam sessions they are conducting
        - Jam sessions of which they are a member
        - All public (i.e., not unlisted) jam sessions

        Admins can view all jam sessions.
        """

        if self.request.user.is_staff:
            return JamSession.objects.all()

        conditions = (
            Q(conductor__pk=self.request.user.id) |
            Q(is_unlisted=False) |
            Q(members__id=self.request.user.id)
        )

        return JamSession.objects.filter(conditions).distinct()


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


class PartDefinitionViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = PartDefinition.objects.all()
    serializer_class = PartDefinitionSerializer


class SongPartViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = SongPart.objects.all()
    serializer_class = SongPartSerializer


class SongPartPageViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = SongPartPage.objects.all()
    serializer_class = SongPartPageSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Relationship views

class JamSessionRelationshipView(RelationshipView):
    queryset = JamSession.objects.all()


class JamSessionRelationshipViewMembers(JamSessionRelationshipView):
    permission_classes = (IsConductorOrAdminOrReadOnly,)
    resource_name = "jamSession"


class JamSessionRelationshipViewSongs(JamSessionRelationshipView):
    permission_classes = (IsConductorOrAdminOrReadOnly,)
    resource_name = "jamSession"


class SongRelationshipView(RelationshipView):
    queryset = Song.objects.all()


class JamSessionSongRelationshipView(RelationshipView):
    queryset = JamSessionSong.objects.all()


class SongPartRelationshipView(RelationshipView):
    queryset = SongPart.objects.all()


class SongPartPageRelationshipView(RelationshipView):
    queryset = SongPartPage.objects.all()
