from django.test import TestCase, Client
import django.urls


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        full_url = django.urls.reverse("about:about")
        response = Client().get(full_url)
        self.assertEqual(response.status_code, 200)
