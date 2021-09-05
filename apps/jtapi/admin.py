from django.contrib import admin
from .models import (
    JamSession, JamSessionMembership, SongProvider, Song, PartDefinition, SongPart
)

class JamSessionMembershipInline(admin.TabularInline):
    model = JamSessionMembership


@admin.register(JamSession)
class JamSessionAdmin(admin.ModelAdmin):
    inlines = [JamSessionMembershipInline]


@admin.register(SongProvider)
class SongProviderAdmin(admin.ModelAdmin):
    model = SongProvider


@admin.register(PartDefinition)
class PartDefinitionAdmin(admin.ModelAdmin):
    model = PartDefinition


class SongPartInline(admin.StackedInline):
    model = SongPart
    show_change_link = True


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    model = Song
    inlines = [
        SongPartInline,
    ]
