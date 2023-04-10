# flashcards views
from django.shortcuts import (
    HttpResponseRedirect,
    get_object_or_404,
    render
)
from django.urls import reverse
from .models import Card_Set, Card
from .forms import Card_Set_Form, Card_Form



def flashcards(request):
    topic_query_set = Card_Set.objects.all().order_by('topic').filter(is_active=True)
    context = {'topics': topic_query_set}
    return render(request, 'flashcards/flashcards.html', context)


def create_card_set(request):
    if request.method == 'POST':
        form = Card_Set_Form(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flashcards'))

    else:
        form = Card_Set_Form()

    context = {'form': form}
    return render(request, 'flashcards/create_card_set.html', context)


def create_card(request, card_set_id):
    card_set_object = get_object_or_404(Card_Set, id=card_set_id)

    if request.method == 'POST':
        form = Card_Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flashcards'))

    else:
        form = Card_Form(initial={'parent_card_set': card_set_object})

    context = {'form': form}
    return render(request, 'flashcards/add_edit_cards.html', context)


def delete_card(request, card_id):

    card_object = get_object_or_404(Card, id=card_id)
    card_object.delete()
    return HttpResponseRedirect(reverse('flashcards'))


def delete_card_set(request, card_set_id):
    card_set_object = get_object_or_404(Card_Set, id=card_set_id)
    card_set_object.delete()
    return HttpResponseRedirect(reverse('flashcards'))


def edit_card(request, card_id):
    card_object = get_object_or_404(Card, id=card_id)

    if request.method == 'POST':
        form = Card_Form(request.POST, instance=card_object)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flashcards'))

    else:
        form = Card_Form(instance=card_object)

    context = {'form': form, 'edit_mode': True, 'card_object': card_object}
    return render(request, 'flashcards/add_edit_cards.html', context)


def edit_card_set(request, card_set_id):
    card_set_object = get_object_or_404(Card_Set, id=card_set_id)

    if request.method == 'POST':
        form = Card_Set_Form(request.POST, instance=card_set_object)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('flashcards'))

    else:
        form = Card_Set_Form(instance=card_set_object)

    context = {'form': form, 'edit_mode': True, 'card_set_object': card_set_object}
    return render(request, 'flashcards/create_card_set.html', context)


def view_card_set(request, card_set_id):
    card_set_object = get_object_or_404(Card_Set, id=card_set_id)
    card_list = card_set_object.card_set.all()
    card_object = card_list.first()

    if request.method == 'GET' and 'card' in request.GET:
        card_object = get_object_or_404(Card, id=request.GET['card'])

    context = {'card_set_object': card_set_object, 'card_object': card_object}
    return render(request, 'flashcards/view_cards.html', context)


