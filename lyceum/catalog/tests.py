import django.core.exceptions
import django.test
import django.urls

import catalog.models

"""
class StaticURLTests(django.test.TestCase):
    def test_catalog_endpoint(self):
        full_url = django.urls.reverse("catalog:item_list")
        response = django.test.Client().get(full_url)
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
        ]
    )
    def test_catalog_item_endpoint(self, url, expected_status):
        try:
            full_url = django.urls.reverse("catalog:item_detail", args=(url,))
            response = django.test.Client().get(full_url)
            self.assertEqual(response.status_code, expected_status)
        except django.urls.exceptions.NoReverseMatch:
            pass

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
                ],
            ),
        )
    )
    def test_catalog_item_positive_integer_endpoint(
        self, prefix, url, expected_status
    ):
        try:
            full_url = django.urls.reverse(
                "catalog:catalog-item-pos-int-name",
                args=(
                    prefix,
                    url,
                ),
            )
            response = django.test.Client().get(full_url)
            self.assertEqual(
                response.status_code,
                expected_status,
                f"Failed to check status request to '{full_url}'",
            )
        except django.urls.exceptions.NoReverseMatch:
            pass


class ModelsTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = catalog.models.Category.objects.create(
            id=1,
            is_published=True,
            name="Тестовая категория",
            slug="test-category-slug",
            weight=100,
        )

        cls.tag = catalog.models.Tag.objects.create(
            id=1,
            is_published=True,
            name="Тестовый тэг",
            slug="test-tag-slug",
        )

    def test_create(self):
        item_count = catalog.models.Item.objects.count()

        self.item = catalog.models.Item(
            id=1,
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
            id=1,
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
        self.item = catalog.models.Item(
            id=1,
            name="Тестовый товар",
            category=self.category,
            text="обычное тестирование",
        )

        self.assertRaises(django.core.exceptions.ValidationError)

"""


class ContextTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.published_category = catalog.models.Category.objects.create(
            id=100,
            is_published=True,
            name="Тестовая опубликованная категория",
            slug="published_category",
            weight=100,
        )
        cls.unpublished_category = catalog.models.Category.objects.create(
            id=101,
            is_published=False,
            name="Тестовая неопубликованная категория",
            slug="unpublished_category",
            weight=100,
        )
        cls.published_tag = catalog.models.Tag.objects.create(
            id=100,
            is_published=True,
            name="Тестовый опубликованный тег",
            slug="published_tag",
        )
        cls.unpublished_tag = catalog.models.Tag.objects.create(
            id=101,
            is_published=False,
            name="Тестовый неопубликованный тег",
            slug="unpublished_tag",
        )
        cls.published_item = catalog.models.Item(
            id=100,
            is_published=True,
            name="Тестовый опубликованный товар",
            text="превосходно",
            category=cls.published_category,
        )
        cls.unpublished_item = catalog.models.Item(
            id=101,
            is_published=False,
            name="Тестовый неопубликованный товар",
            text="превосходно",
            category=cls.published_category,
        )

        cls.published_category.save()
        cls.unpublished_category.save()

        cls.published_tag.save()
        cls.unpublished_tag.save()

        cls.published_item.clean()
        cls.published_item.save()
        cls.unpublished_item.clean()
        cls.unpublished_item.save()

        cls.published_item.tags.add(cls.published_tag.pk)
        cls.published_item.tags.add(cls.unpublished_tag.pk)

    def test_home_page_show_correct_context(self):
        response = django.test.Client().get(
            django.urls.reverse("homepage:home")
        )
        self.assertIn("items", response.context)
