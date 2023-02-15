from django.http import HttpResponse


def home(request):
    return HttpResponse("<body>This is a homepage</body>")
