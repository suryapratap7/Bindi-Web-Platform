from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>This is where we will test a database connection.</H1>")
