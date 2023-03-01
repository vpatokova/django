from django.shortcuts import render


def project_description(request):
    template = "about/project_description.html"
    context = {}
    return render(request, template, context)
