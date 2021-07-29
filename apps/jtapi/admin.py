from django.contrib import admin
from .models import JamSession, JamSessionMembership, SongProvider

class JamSessionMembershipInline(admin.TabularInline):
    model = JamSessionMembership

class JamSessionAdmin(admin.ModelAdmin):
    inlines = [JamSessionMembershipInline]

class SongProviderAdmin(admin.ModelAdmin):
    model = SongProvider

admin.site.register(JamSession, JamSessionAdmin)
admin.site.register(SongProvider, SongProviderAdmin)
