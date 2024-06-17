from django.contrib import admin
import nested_admin
from .models import (
    JamSession, JamSessionMembership, SongProvider, Song, PartDefinition, SongPart,
    SongPartPage, JamSessionSong
)

class JamSessionMembershipInline(admin.TabularInline):
    model = JamSessionMembership


class JamSessionSongInline(admin.StackedInline):
    model = JamSessionSong

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(state='Queued')


@admin.register(JamSession)
class JamSessionAdmin(admin.ModelAdmin):
    inlines = [
        JamSessionMembershipInline,
        JamSessionSongInline,
    ]


@admin.register(SongProvider)
class SongProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(PartDefinition)
class PartDefinitionAdmin(admin.ModelAdmin):
    pass


class SongPartPageInline(nested_admin.NestedStackedInline):
    model = SongPartPage
    extra = 0


class SongPartInline(nested_admin.NestedStackedInline):
    model = SongPart
    inlines = [
        SongPartPageInline,
    ]
    extra = 0


@admin.register(Song)
class SongAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        SongPartInline,
    ]


@admin.register(JamSessionSong)
class JamSessionSongAdmin(admin.ModelAdmin):
    pass
