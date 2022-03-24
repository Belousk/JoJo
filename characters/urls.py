from django.urls import path

import characters
from . import views

urlpatterns = [
    path("<character>", views.character)
]
