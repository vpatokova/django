from django.core.mail import send_mail
from django.shortcuts import render, redirect

from feedback.forms import FeedbackForm

from lyceum.settings import EMAIL_HOST


def feedback(request):
    template = "feedback/feedback.html"
    form = FeedbackForm(request.POST or None)

    if form.is_valid():
        text = form.cleaned_data.get("text")
        mail = form.cleaned_data.get("mail")
        send_mail(
            subject="Thank you for your feedback!",
            message=f"We got your feedback '{text}'",
            from_email=EMAIL_HOST,
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
