from django.urls import path
from rest_framework import routers
from apps.jtapi.views import (
    JamSessionViewSet,
    PartDefinitionViewSet,
    UserViewSet,
    SongProviderViewSet,
    SongViewSet,
    JamSessionSongViewSet,
    SongPartViewSet,
    SongPartPageViewSet,
    JamSessionRelationshipView,
    JamSessionRelationshipViewCurrentSong,
    JamSessionRelationshipViewMembers,
    JamSessionRelationshipViewQueuedSongs,
    JamSessionSongRelationshipView,
    SongRelationshipView,
    SongPartRelationshipView,
    SongPartPageRelationshipView,
)

router = routers.DefaultRouter()
router.register(r'jam-sessions', JamSessionViewSet)
router.register(r'part-definitions', PartDefinitionViewSet)
router.register(r'song-providers', SongProviderViewSet)
router.register(r'songs', SongViewSet)
router.register(r'jam-session-songs', JamSessionSongViewSet)
router.register(r'song-parts', SongPartViewSet)
router.register(r'song-part-pages', SongPartPageViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls + [
    # API relationships
    path(
        'jam-sessions/<int:pk>/relationships/members/',
        JamSessionRelationshipViewMembers.as_view(),
        { "related_field": "members" },
        name='jamsession-relationships',
    ),

    path(
        'jam-sessions/<int:pk>/relationships/queued-songs/',
        JamSessionRelationshipViewQueuedSongs.as_view(),
        { "related_field": "queued_songs" },
        name='jamsession-relationships',
    ),

    path(
        'jam-sessions/<int:pk>/relationships/current-song/',
        JamSessionRelationshipViewCurrentSong.as_view(),
        { "related_field": "current_song" },
        name='jamsession-relationships',
    ),

    path(
        'jam-sessions/<int:pk>/relationships/<related_field>/',
        JamSessionRelationshipView.as_view(),
        name='jamsession-relationships',
    ),

    path(
        'songs/<int:pk>/relationships/<related_field>/',
        SongRelationshipView.as_view(),
        name='song-relationships',
    ),

    path(
        'jam-session-songs/<int:pk>/relationships/<related_field>',
        JamSessionSongRelationshipView.as_view(),
        name='jamsessionsong-relationships',
    ),

    path(
        'song-parts/<int:pk>/relationships/<related_field>/',
        SongPartRelationshipView.as_view(),
        name='songpart-relationships',
    ),

    path(
        'song-part-pages/<int:pk>/relationships/<related_field>/',
        SongPartPageRelationshipView.as_view(),
        name='songpartpage-relationships',
    ),

    # API related URLs
    path(
        'jam-sessions/<int:pk>/<related_field>/',
        JamSessionViewSet.as_view({'get': 'retrieve_related'}),
        name='jamsession-related',
    ),

    path(
        'songs/<int:pk>/<related_field>/',
        SongViewSet.as_view({'get': 'retrieve_related'}),
        name='song-related',
    ),

    path(
        'jam-session-songs/<int:pk>/<related_field>/',
        JamSessionSongViewSet.as_view({'get': 'retrieve_related'}),
        name='jamsessionsong-related',
    ),

    path(
        'song-parts/<int:pk>/<related_field>/',
        SongPartViewSet.as_view({'get': 'retrieve_related'}),
        name='songpart-related',
    ),

    path(
        'song-part-pages/<int:pk>/<related_field>/',
        SongPartPageViewSet.as_view({'get': 'retrieve_related'}),
        name='songpartpage-related',
    ),
]
