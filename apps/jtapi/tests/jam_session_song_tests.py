from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from apps.jtapi.models import JamSession, Song, SongProvider
from apps.jtapi.views import JamSessionRelationshipViewSongs
from unittest import skip

# TODO: Improve setup for better readability

@skip("Need to figure out what we actually want to test here")
class JamSessionRelationshipViewSongsTestCase(TestCase):
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

        self.view = JamSessionRelationshipViewSongs.as_view()

    def test_admin_can_add_song_to_song_list(self):
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
            "/jam-sessions/1/relationships/songs",
            data=request_data,
            format="vnd.api+json",
        )
        force_authenticate(request, user=self.admin_user)

        response = self.view(
            request,
            pk=self.jam_session.pk,
            related_field="songs",
        )

        print(response)

        self.assertEqual(response.status_code, 200)
