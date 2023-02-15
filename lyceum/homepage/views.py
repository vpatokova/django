from django.http import HttpResponse


def home(request):
    return HttpResponse("<body>This is a homepage</body>")


def coffee(request):
    return HttpResponse("<body>I am a teapot</body>", status=418)
