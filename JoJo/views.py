from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello visitor! enter ')


def page_not_found_view(request, exception):
    return render(request, 'character/page_not_found.html', status=404)
