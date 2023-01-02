from rest_framework_json_api.views import ModelViewSet, RelationshipView
from django.db.models import Q

from ..models import JamSession
from ..permissions import IsConductorOrAdminOrReadOnly
from ..serializers import JamSessionSerializer

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


class JamSessionRelationshipView(RelationshipView):
    queryset = JamSession.objects.all()


class JamSessionRelationshipViewMembers(JamSessionRelationshipView):
    permission_classes = (IsConductorOrAdminOrReadOnly,)
    resource_name = "jamSession"


class JamSessionRelationshipViewSongs(JamSessionRelationshipView):
    permission_classes = (IsConductorOrAdminOrReadOnly,)
    resource_name = "jamSession"
