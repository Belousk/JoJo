from django.http import HttpResponse
from django.shortcuts import render


def character(request, name):
    if dct.get(name):
        data = {
            'name': name,
            'intro': dct.get(name)['intro'],
            'info': dct.get(name)['description']
        }
        return render(request, 'characters/character.html', context=data)
    else:
        return HttpResponseRedirect('404')
