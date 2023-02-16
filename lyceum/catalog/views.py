from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>This is the list of items</body>")


def item_detail(request, pk):
    return HttpResponse("<body>About the selected item in details</body>")


def new_page(request):
    return HttpResponse("<body>Я родился!</body>")


def converter(request, year, number):
    return HttpResponse(f"<body>I'm a converter!. Year is {year}, number is {number}</body>")
