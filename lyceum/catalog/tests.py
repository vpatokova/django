import itertools

import django.core.exceptions
import django.test
import parameterized

import catalog.models


class StaticURLTests(django.test.TestCase):
    def test_catalog_endpoint(self):
        response = django.test.Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    @parameterized.parameterized.expand(
        [
            ("1", 200),
            ("100", 200),
            ("0", 200),
            ("-0", 404),
            ("0.5", 404),
            ("abc", 404),
            ("0abc", 404),
            ("abc0", 404),
            ("$%^", 404),
            ("1e5", 404),
        ]
    )
    def test_catalog_item_endpoint(self, url, expected_status):
        response = django.test.Client().get(f"/catalog/{url}")
        self.assertEqual(response.status_code, expected_status)

    @parameterized.parameterized.expand(
        map(
            lambda x: (x[0], x[1][0], x[1][1]),
            itertools.product(
                [
                    "dog",
                    "fog",
                    "re",
                ],
                [
                    ("1", 200),
                    ("100", 200),
                    ("0", 404),
                    ("-0", 404),
                    ("0.5", 404),
                    ("abc", 404),
                    ("0abc", 404),
                    ("abc0", 404),
                    ("$%^", 404),
                    ("1e5", 404),
                ],
            ),
        )
    )
    def test_catalog_item_positive_integer_endpoint(
        self,
        prefix,
        url,
        expected_status
    ):
        full_url = f"/catalog/{prefix}/{url}"
        response = django.test.Client().get(full_url)
        self.assertEqual(
            response.status_code,
            expected_status,
            f"Failed to check status request to '{full_url}'",
        )


class ModelsTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name="Тестовая категория",
            slug="test-category-slug",
            weight=100,
        )

        cls.tag = catalog.models.Tag.objects.create(
            is_published=True, name="Тестовый тэг", slug="test-tag-slug"
        )

    def test_create(self):
        item_count = catalog.models.Item.objects.count()

        self.item = catalog.models.Item(
            name="Тестовый товар",
            category=self.category,
            text="роскошное тестирование",
        )
        self.item.tags.add(ModelsTests.tag)
        self.item.full_clean()
        self.item.save()

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count + 1,
        )

    def test_positive_validator(self):
        item_count = catalog.models.Item.objects.count()

        self.item = catalog.models.Item(
            name="Тестовый товар",
            category=self.category,
            text="превосходное тестирование",
        )
        self.item.tags.add(ModelsTests.tag)
        self.item.full_clean()
        self.item.save()

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count + 1,
        )

    def test_negative_validator(self):
        item_count = catalog.models.Item.objects.count()

        self.item = catalog.models.Item(
            name="Тестовый товар",
            category=self.category,
            text="обычное тестирование",
        )
        self.item.tags.add(ModelsTests.tag)
        self.item.full_clean()
        self.item.save()

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count,
        )
