"""jamtogether URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
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

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

    # API relationships
    path(
        'api/jam-sessions/<int:pk>/relationships/members/',
        JamSessionRelationshipViewMembers.as_view(),
        { "related_field": "members" },
        name='jamsession-relationships',
    ),

    path(
        'api/jam-sessions/<int:pk>/relationships/queued-songs/',
        JamSessionRelationshipViewQueuedSongs.as_view(),
        { "related_field": "queued_songs" },
        name='jamsession-relationships',
    ),

    path(
        'api/jam-sessions/<int:pk>/relationships/current-song/',
        JamSessionRelationshipViewCurrentSong.as_view(),
        { "related_field": "current_song" },
        name='jamsession-relationships',
    ),

    path(
        'api/jam-sessions/<int:pk>/relationships/<related_field>/',
        JamSessionRelationshipView.as_view(),
        name='jamsession-relationships',
    ),

    path(
        'api/songs/<int:pk>/relationships/<related_field>/',
        SongRelationshipView.as_view(),
        name='song-relationships',
    ),

    path(
        'api/jam-session-songs/<int:pk>/relationships/<related_field>',
        JamSessionSongRelationshipView.as_view(),
        name='jamsessionsong-relationships',
    ),

    path(
        'api/song-parts/<int:pk>/relationships/<related_field>/',
        SongPartRelationshipView.as_view(),
        name='songpart-relationships',
    ),

    path(
        'api/song-part-pages/<int:pk>/relationships/<related_field>/',
        SongPartPageRelationshipView.as_view(),
        name='songpartpage-relationships',
    ),

    # API related URLs
    path(
        'api/jam-sessions/<int:pk>/<related_field>/',
        JamSessionViewSet.as_view({'get': 'retrieve_related'}),
        name='jamsession-related',
    ),

    path(
        'api/songs/<int:pk>/<related_field>/',
        SongViewSet.as_view({'get': 'retrieve_related'}),
        name='song-related',
    ),

    path(
        'api/jam-session-songs/<int:pk>/<related_field>/',
        JamSessionSongViewSet.as_view({'get': 'retrieve_related'}),
        name='jamsessionsong-related',
    ),

    path(
        'api/song-parts/<int:pk>/<related_field>/',
        SongPartViewSet.as_view({'get': 'retrieve_related'}),
        name='songpart-related',
    ),

    path(
        'api/song-part-pages/<int:pk>/<related_field>/',
        SongPartPageViewSet.as_view({'get': 'retrieve_related'}),
        name='songpartpage-related',
    ),
]
