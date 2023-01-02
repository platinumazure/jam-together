from rest_framework_json_api.views import ModelViewSet, RelationshipView
from ..models import PartDefinition, SongPart, SongPartPage
from ..permissions import IsAdminOrReadOnly
from ..serializers import (
    PartDefinitionSerializer,
    SongPartSerializer,
    SongPartPageSerializer,
)

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


class SongPartRelationshipView(RelationshipView):
    queryset = SongPart.objects.all()


class SongPartPageRelationshipView(RelationshipView):
    queryset = SongPartPage.objects.all()
