from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Guy hamalch </h1>")
# Create your views here.
