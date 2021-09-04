from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField
from django.contrib.auth.models import User
from .models import JamSession, SongProvider, Song, PartDefinition

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'last_login', 'date_joined', 'url',
        ]


class JamSessionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='jamsession-detail')

    conductor = ResourceRelatedField(
        queryset=User.objects,
        related_link_view_name='jamsession-related',
        self_link_view_name='jamsession-relationships',
    )

    created_by = ResourceRelatedField(
        queryset=User.objects,
        related_link_view_name='jamsession-related',
        self_link_view_name='jamsession-relationships',
    )

    members = ResourceRelatedField(
        queryset=User.objects,
        many=True,
        related_link_view_name='jamsession-related',
        self_link_view_name='jamsession-relationships',
    )

    related_serializers = {
        'conductor': UserSerializer,
        'created_by': UserSerializer,
        'members': UserSerializer,
    }

    class Meta:
        model = JamSession
        fields = '__all__'


class SongProviderSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='songprovider-detail')

    songs = ResourceRelatedField(
        queryset=Song.objects,
        many=True,
    )

    included_serializers = {
        'songs': 'apps.jtapi.serializers.SongSerializer',
    }

    class Meta:
        model = SongProvider
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='song-detail')

    song_provider = ResourceRelatedField(
        queryset=SongProvider.objects,
        related_link_view_name='song-related',
        self_link_view_name='song-relationships',
    )

    related_serializers = {
        'song_provider': SongProviderSerializer,
    }

    class Meta:
        model = Song
        fields = '__all__'


class PartDefinitionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='partdefinition-detail')

    class Meta:
        model = PartDefinition
        fields = '__all__'
