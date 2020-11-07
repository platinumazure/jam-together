from django.contrib import admin
from .models import JamSession, JamSessionMembership

class JamSessionMembershipInline(admin.TabularInline):
    model = JamSessionMembership

class JamSessionAdmin(admin.ModelAdmin):
    inlines = [JamSessionMembershipInline]

admin.site.register(JamSession, JamSessionAdmin)
