"""jamtogether URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apps.jtapi.views import JamSessionViewSet

router = routers.DefaultRouter()
router.register(r'jam-sessions', JamSessionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
