from django.contrib import admin
from .models import JamSession, JamSessionMembership, SongProvider

class JamSessionMembershipInline(admin.TabularInline):
    model = JamSessionMembership


@admin.register(JamSession)
class JamSessionAdmin(admin.ModelAdmin):
    inlines = [JamSessionMembershipInline]


@admin.register(SongProvider)
class SongProviderAdmin(admin.ModelAdmin):
    model = SongProvider
