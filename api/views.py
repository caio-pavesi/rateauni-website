"""Lorem ipsum"""

from django.http import HttpResponse

def home(request):
    "Lorem ipsum"
    return HttpResponse("Hello, World!")
