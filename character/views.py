from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .data.character_info import CHARACTER_INFORMATION


def character(request, name):
    character_data = CHARACTER_INFORMATION.get(name.replace('_', ' '))
    print(name)
    if character_data:
        data = {
            'name': name.replace('_', ' '),
            'info': character_data['description'],
            'img': character_data['photo']
        }
        return render(request, 'character/character.html', context=data)
    else:
        return render(request, 'character/page_not_found.html')


def character_list(request):
    names = CHARACTER_INFORMATION.keys()
    context = {
        'names': [[name.replace(' ', '_'), name] for name in names]
    }
    return render(request, 'character/character_list.html', context=context)


