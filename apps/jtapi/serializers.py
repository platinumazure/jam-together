from rest_framework_json_api import serializers
from .models import JamSession

class JamSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JamSession
        fields = '__all__'
