from django.core.mail import send_mail
from django.shortcuts import render, redirect
import django.conf

from feedback.forms import FeedbackForm


EMAIL_SUBJECT_TEXT: str = "Thanks"
EMAIL_RESPONSE_TEXT: str = "Thank you for your feedback: \n\n{text}. \n\n"
"Your opinion is very important to us"


def feedback(request):
    template = "feedback/feedback.html"
    form = FeedbackForm(request.POST or None)

    if form.is_valid():
        text = form.cleaned_data.get("text")
        mail = form.cleaned_data.get("mail")
        send_mail(
            subject=EMAIL_SUBJECT_TEXT,
            message=EMAIL_RESPONSE_TEXT.format(text=text),
            from_email=django.conf.settings.EMAIL_HOST,
            recipient_list=[mail],
            fail_silently=False,
        )

        return redirect("feedback:thanks")
    context = {
        "form": form,
    }
    return render(request, template, context)


def thanks(request):
    template = "feedback/thanks.html"
    context = {
        "text": "Спасибо, ваш отзыв очень важен для нас (вообще-то нет)",
    }
    return render(request, template, context)
