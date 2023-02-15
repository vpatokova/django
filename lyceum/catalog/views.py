from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>This is the list of items</body>")


def item_detail(request, pk):
    return HttpResponse("<body>About the selected item in details</body>")
