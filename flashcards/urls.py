from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .views import *


urlpatterns = [
    path('', flashcards, name = 'flashcards'),
    path('create/', create_card_set, name = 'create_card_set'),
    path('create_card/(?P<card_set_id>[\d]+)', create_card, name = 'create_card'),
    path('delete/(?P<card_set_id>[\d]+)', delete_card_set, name = 'delete_card_set'),
    path('delete_card/(?P<card_id>[\d]+)', delete_card, name = 'delete_card'),
    path('edit/(?P<card_set_id>[\d]+)', edit_card_set, name = 'edit_card_set'),
    path('edit_card/(?P<card_id>[\d]+)', edit_card, name = 'edit_card'),
    path('view/(?P<card_set_id>[\d]+)', view_card_set, name = 'view_card_set'),

]