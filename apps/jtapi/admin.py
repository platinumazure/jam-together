from django.contrib import admin
from .models import (
    JamSession, JamSessionMembership, SongProvider, Song, PartDefinition, SongPart,
    SongPartPage,
)

class JamSessionMembershipInline(admin.TabularInline):
    model = JamSessionMembership


@admin.register(JamSession)
class JamSessionAdmin(admin.ModelAdmin):
    inlines = [JamSessionMembershipInline]


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
