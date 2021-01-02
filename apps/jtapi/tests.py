from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from .models import JamSession
from .views import JamSessionViewSet

# TODO: Move into a tests package
# TODO: Improve setup for better readability
# TODO: Determine why `python manage.py test` does not find these tests

class JamSessionViewTestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username="admin", password="admin")
        self.conductor = User.objects.create_user(username="conductor", password="conductor")
        self.member = User.objects.create_user(username="member", password="member")
        self.non_member = User.objects.create_user(username="nonmember", password="nonmember")

        self.listed_jam_session = JamSession.objects.create(
            name="Test jam",
            conductor=self.conductor,
            is_unlisted=False,
            created_by=self.admin_user,
        )

        self.listed_jam_session.members.add(self.member)

        self.unlisted_jam_session = JamSession.objects.create(
            name="Test jam",
            conductor=self.conductor,
            is_unlisted=True,
            created_by=self.admin_user,
        )

        self.unlisted_jam_session.members.add(self.member)

        self.factory = APIRequestFactory()

        self.view = JamSessionViewSet.as_view({"get": "retrieve"})

    def test_admin_can_see_listed_jam(self):
        request = self.factory.get("")
        force_authenticate(request, user=self.admin_user)

        response = self.view(request, pk=self.listed_jam_session.id)

        self.assertEqual(response.status_code, 200)

    def test_admin_can_see_unlisted_jam(self):
        request = self.factory.get("")
        force_authenticate(request, user=self.admin_user)

        response = self.view(request, pk=self.unlisted_jam_session.id)

        self.assertEqual(response.status_code, 200)

    def test_conductor_can_see_listed_jam(self):
        request = self.factory.get("")
        force_authenticate(request, user=self.conductor)

        response = self.view(request, pk=self.listed_jam_session.id)

        self.assertEqual(response.status_code, 200)

    def test_conductor_can_see_unlisted_jam(self):
        request = self.factory.get("")
        force_authenticate(request, user=self.conductor)

        response = self.view(request, pk=self.unlisted_jam_session.id)

        self.assertEqual(response.status_code, 200)

    def test_jam_member_can_see_listed_jam(self):
        request = self.factory.get("")
        force_authenticate(request, user=self.member)

        response = self.view(request, pk=self.listed_jam_session.id)

        self.assertEqual(response.status_code, 200)

    def test_jam_member_can_see_unlisted_jam(self):
        request = self.factory.get("")
        force_authenticate(request, user=self.member)

        response = self.view(request, pk=self.unlisted_jam_session.id)

        self.assertEqual(response.status_code, 200)

    def test_jam_non_member_can_see_listed_jam(self):
        request = self.factory.get("")
        force_authenticate(request, user=self.non_member)

        response = self.view(request, pk=self.listed_jam_session.id)

        self.assertEqual(response.status_code, 200)

    def test_jam_non_member_cannot_see_unlisted_jam(self):
        request = self.factory.get("")
        force_authenticate(request, user=self.non_member)

        response = self.view(request, pk=self.unlisted_jam_session.id)

        self.assertEqual(response.status_code, 404)
