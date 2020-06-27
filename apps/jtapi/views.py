from rest_framework import viewsets
from .models import JamSession
from .serializers import JamSessionSerializer

class JamSessionViewSet(viewsets.ModelViewSet):
    queryset = JamSession.objects.all()
    serializer_class = JamSessionSerializer
