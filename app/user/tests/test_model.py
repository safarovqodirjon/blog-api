from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTest(TestCase):
    def setUp(self):
        """create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="password123",
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="password123",
            name="Test user",
        )

    def test_edit_user_page(self):
        url = reverse("admin:user_user_change", args=[self.user.uuid])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_page(self):
        url = reverse("admin:user_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
