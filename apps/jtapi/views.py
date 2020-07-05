from rest_framework_json_api.views import ModelViewSet, ReadOnlyModelViewSet, RelationshipView
from django.contrib.auth.models import User
from .models import JamSession
from .serializers import JamSessionSerializer, UserSerializer

class JamSessionViewSet(ModelViewSet):
    queryset = JamSession.objects.all()
    serializer_class = JamSessionSerializer

class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Relationship views

class JamSessionRelationshipView(RelationshipView):
    queryset = JamSession.objects.all()
