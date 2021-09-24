from django.contrib import admin
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


class SongPartInline(admin.StackedInline):
    model = SongPart
    show_change_link = True


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    inlines = [
        SongPartInline,
    ]


class SongPartPageInline(admin.StackedInline):
    model = SongPartPage


@admin.register(SongPart)
class SongPartAdmin(admin.ModelAdmin):
    inlines = [
        SongPartPageInline,
    ]


@admin.register(JamSessionSong)
class JamSessionSongAdmin(admin.ModelAdmin):
    pass
