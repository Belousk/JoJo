from django.urls import path

import character
from . import views

urlpatterns = [
    path('list', views.character_list),
    path("<name>", views.character)
]
