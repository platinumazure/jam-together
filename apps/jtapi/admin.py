from django.contrib import admin
from .models import JamSession, JamSessionMembership, SongProvider, Song, PartDefinition

class JamSessionMembershipInline(admin.TabularInline):
    model = JamSessionMembership


@admin.register(JamSession)
class JamSessionAdmin(admin.ModelAdmin):
    inlines = [JamSessionMembershipInline]


@admin.register(SongProvider)
class SongProviderAdmin(admin.ModelAdmin):
    model = SongProvider


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    model = Song


@admin.register(PartDefinition)
class PartAdmin(admin.ModelAdmin):
    model = PartDefinition
