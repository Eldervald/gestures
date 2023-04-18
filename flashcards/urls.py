from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .views import *


urlpatterns = [

    path('', flashcards, name = 'flashcards'),
    path('create/', create_card_set, name = 'create_card_set'),
    path('create_card/<int:card_set_id>/', create_card, name='create_card'),
    path('delete/<int:card_set_id>/', delete_card_set, name='delete_card_set'),
    path('delete_card/<int:card_id>/', delete_card, name='delete_card'),
    path('edit/<int:card_set_id>/', edit_card_set, name='edit_card_set'),
    path('edit_card/<int:card_id>/', edit_card, name='edit_card'),
    path('view/<int:card_set_id>/', view_card_set, name='view_card_set'),
]