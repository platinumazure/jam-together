from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, force_authenticate
from apps.jtapi.models import JamSession, Song, SongProvider
from apps.jtapi.views import JamSessionSongViewSet
from unittest import skip

User = get_user_model()

class JamSessionSongViewSetTestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username="admin", password="admin")
        self.conductor = User.objects.create_user(username="conductor", password="conductor")
        self.member = User.objects.create_user(username="member", password="member")
        self.non_member = User.objects.create_user(username="nonmember", password="nonmember")

        self.jam_session = JamSession.objects.create(
            name="Test jam",
            conductor=self.conductor,
            is_unlisted=False,
            created_by=self.admin_user,
        )

        self.song_provider = SongProvider.objects.create(
            name="Fake provider",
            description="Fake provider description",
            site_url="http://example.com",
        )

        self.song = Song.objects.create(
            title="Test song",
            song_provider=self.song_provider,
        )

        self.jam_session.members.add(self.member)

        self.factory = APIRequestFactory()

        self.view = JamSessionSongViewSet.as_view({ "get": "list", "post": "create" })

    def test_create_permissions(self):
        params = {
            "admin": (self.admin_user, 201),
            "conductor": (self.conductor, 201),
            "member": (self.member, 403),
            "nonmember": (self.non_member, 403),
        }

        for scenario, (user, expected_code) in params.items():
            with self.subTest(scenario):
                request_data = {
                    "data": {
                        "type": "jamSessionSong",
                        "attributes": {},
                        "relationships": {
                            "jam_session": {
                                "data": { "id": self.jam_session.id, "type": "jamSession" }
                            },
                            "song": {
                                "data": { "id": self.song.id, "type": "song" }
                            }
                        }
                    }
                }

                request = self.factory.post(
                    "/jam-session-songs/",
                    data=request_data,
                    format="vnd.api+json",
                )
                force_authenticate(request, user=user)

                response = self.view(request)

                self.assertEqual(response.status_code, expected_code)
