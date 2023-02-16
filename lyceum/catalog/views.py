from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>This is the list of items</body>")


def item_detail(request, pk):
    return HttpResponse("<body>About the selected item in details</body>")


def new_page(request):
    return HttpResponse("<body>Я родился!</body>")


def try_converter(request, text: str, pk: int):
    return HttpResponse("<body>I'm a converter!</body>")
