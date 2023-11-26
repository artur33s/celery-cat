from django.http import HttpResponse

# Create your views here.
from . import tasks


def home(request):
    tasks.download_cat.delay()
    # start a task
    return HttpResponse("<h1>Load Cats</h1>")
