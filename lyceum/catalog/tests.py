from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog")
        self.assertEqual(response.status_code, 200)

    def test_new_page_endpoint(self):
        response = Client().get("/catalog/<int:pk>")
        self.assertEqual(response.status_code, 200)

    def test_converter_endpoint(self):
        response = Client().get("/catalog/<yyyy:year>/<pn:number>")
        self.assertEqual(response.status_code, 200)


