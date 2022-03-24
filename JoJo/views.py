from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello visitor! enter ')


def not_found_page(request):
    return render(request, 'character/page_not_found.html')
