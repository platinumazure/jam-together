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
    JamSessionRelationshipView,
    JamSessionMembersRelationshipView,
    SongRelationshipView,
)

router = routers.DefaultRouter()
router.register(r'jam-sessions', JamSessionViewSet)
router.register(r'part-definitions', PartDefinitionViewSet)
router.register(r'song-providers', SongProviderViewSet)
router.register(r'songs', SongViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

    # API relationships
    path(
        'api/jam-sessions/<int:pk>/relationships/members/',
        JamSessionMembersRelationshipView.as_view(),
        { "related_field": "members" },
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
]
