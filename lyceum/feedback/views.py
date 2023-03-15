from django.core.mail import send_mail
from django.shortcuts import render, redirect

from feedback.forms import FeedbackForm


def feedback(request):
    template = "feedback/feedback.html"
    form = FeedbackForm(request.POST or None)

    if form.is_valid():
        text = form.cleaned_data.get("text")
        send_mail(
            "Subject here",
            text,
            "from@example.com",
            ["to@example.com"],
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
