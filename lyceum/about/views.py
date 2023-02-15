from django.http import HttpResponse


def item_description(request):
    return HttpResponse("<body>This is the description of the project</body>")
