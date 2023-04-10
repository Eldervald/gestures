from django.contrib import admin
from .models import Card_Set, Card

def push_live(modeladmin, request, query_set):

    rows_updated = query_set.update(is_active = True)

    if rows_updated == 1:
        message = '1 set was'

    else:
        message = '%s were' % rows_updated
    modeladmin.message_user(request, '%s sucessfully updated' % message)

push_live.short_description = 'Select card sets as active.'


class Card_Set_Admin(admin.ModelAdmin):

    list_display = ('topic', 'is_active', 'get_card_count')

    list_filter = ('is_active',)

    search_fields = ['topic', 'description']

    actions = [push_live]

class Card_Admin(admin.ModelAdmin):
    pass

admin.site.register(Card_Set, Card_Set_Admin)
admin.site.register(Card, Card_Admin)