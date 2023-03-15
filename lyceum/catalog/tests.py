import django.core.exceptions
import django.test
import django.urls

import catalog.models
import catalog.forms


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
