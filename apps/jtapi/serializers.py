from rest_framework_json_api import serializers
from rest_framework_json_api.relations import (
    ResourceRelatedField,
    SerializerMethodResourceRelatedField,
)
from django.contrib.auth import get_user_model
from .models import (
    JamSession, SongProvider, Song, PartDefinition, SongPart, SongPartPage,
    JamSessionSong,
)

User = get_user_model()

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

    queued_songs = ResourceRelatedField(
        model=JamSessionSong,
        many=True,
        read_only=True,
        related_link_view_name='jamsession-related',
        self_link_view_name='jamsession-relationships',
    )

    current_song = ResourceRelatedField(
        model=JamSessionSong,
        read_only=True,
        related_link_view_name='jamsession-related',
        self_link_view_name='jamsession-relationships',
    )

    related_serializers = {
        'conductor': UserSerializer,
        'created_by': UserSerializer,
        'current_song': 'apps.jtapi.serializers.JamSessionSongSerializer',
        'members': UserSerializer,
        'queued_songs': 'apps.jtapi.serializers.JamSessionSongSerializer',
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

    parts = ResourceRelatedField(
        queryset=SongPart.objects,
        many=True,
        related_link_view_name='song-related',
        self_link_view_name='song-relationships',
    )

    related_serializers = {
        'song_provider': SongProviderSerializer,
        'parts': 'apps.jtapi.serializers.SongPartSerializer',
    }

    included_serializers = {
        'parts': 'apps.jtapi.serializers.SongPartSerializer',
    }

    class Meta:
        model = Song
        fields = '__all__'


class JamSessionSongSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='jamsessionsong-detail')

    jam_session = ResourceRelatedField(
        queryset=JamSession.objects,
        related_link_view_name='jamsessionsong-related',
        self_link_view_name='jamsessionsong-relationships',
    )

    song = ResourceRelatedField(
        queryset=Song.objects,
        related_link_view_name='jamsessionsong-related',
        self_link_view_name='jamsessionsong-relationships',
    )

    related_serializers = {
        'song': SongSerializer,
        'jam_session': JamSessionSerializer,
    }

    class Meta:
        model = JamSessionSong
        fields = '__all__'


class PartDefinitionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='partdefinition-detail')

    class Meta:
        model = PartDefinition
        fields = '__all__'


class SongPartSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='songpart-detail')

    song = ResourceRelatedField(
        queryset=Song.objects,
        related_link_view_name='songpart-related',
        self_link_view_name='songpart-relationships',
    )

    pages = ResourceRelatedField(
        queryset=SongPartPage.objects,
        many=True,
        related_link_view_name='songpart-related',
        self_link_view_name='songpart-relationships',
    )

    definition = ResourceRelatedField(
        queryset=PartDefinition.objects,
        related_link_view_name='songpart-related',
        self_link_view_name='songpart-relationships',
    )

    related_serializers = {
        'song': SongSerializer,
        'pages': 'apps.jtapi.serializers.SongPartPageSerializer',
        'definition': PartDefinitionSerializer,
    }

    included_serializers = {
        'pages': 'apps.jtapi.serializers.SongPartPageSerializer',
    }

    class Meta:
        model = SongPart
        fields = '__all__'


class SongPartPageSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='songpartpage-detail')

    song_part = ResourceRelatedField(
        queryset=SongPart.objects,
        related_link_view_name='songpartpage-related',
        self_link_view_name='songpartpage-relationships',
    )

    related_serializers = {
        'song_part': SongPartSerializer,
    }

    class Meta:
        model = SongPartPage
        exclude = ['_order']
