import django.core.exceptions
import django.test
import django.urls

import feedback.models
import feedback.forms


class FormTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = feedback.forms.FeedbackForm()

    def test_text_label(self):
        text_label = FormTests.form.fields["text"].label
        self.assertEquals(text_label, "Отзыв")

    def test_mail_label(self):
        mail_label = FormTests.form.fields["mail"].label
        self.assertEquals(mail_label, "Электронная почта")

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
