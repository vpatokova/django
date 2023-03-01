from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    template = "catalog/list.html"
    context = {}
    return render(request, template, context)


def item_detail(request, pk):
    return HttpResponse("<body>About the selected item in details</body>")


def new_page(request):
    return HttpResponse("<body>Я родился!</body>")


def converter(request, text, number):
    return HttpResponse(
        f"<body>I'm a converter!. Text is {text}, number is {number}</body>"
    )
