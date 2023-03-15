import django.core.exceptions
import django.test
import django.urls

import feedback.models
import feedback.forms
import catalog.models


class FormTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = feedback.forms.FeedbackForm()

    def test_name_label(self):
        name_label = FormTests.form.fields["name"].label
        self.assertEquals(name_label, "Имя")

    def test_name_help_text(self):
        name_help_text = FormTests.form.fields["name"].help_text
        self.assertEquals(name_help_text, "Подсказка")

    def test_create_task(self):
        items_count = catalog.models.Item.objects.count()
        form_data = {
            "name": "Тест",
        }

        response = django.test.Client().post(
            django.urls.reverse("feedback:thanks"),
            data=form_data,
            follow=True,
        )

        self.assertRedirects(response, django.urls.reverse("feedback:thanks"))

        self.assertEqual(catalog.models.Item.objects.count(), items_count + 1)
