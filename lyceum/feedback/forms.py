from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            "text",
            "mail",
        )

        labels = {
            "text": "Имя поля",
        }
