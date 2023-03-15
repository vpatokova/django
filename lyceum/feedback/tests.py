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
        name_label = FormTests.form.fields["text"].label
        self.assertEquals(name_label, "Имя поля")

    def test_create_task(self):
        form_data = {
            "text": "Тест",
            "mail": "test@mail.com",
        }

        response = django.test.Client().post(
            django.urls.reverse("feedback:feedback"),
            data=form_data,
            follow=True,
        )

        self.assertRedirects(response, django.urls.reverse("feedback:thanks"))
