from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Decks, Cards
from django.urls import reverse_lazy
from .forms import Add_card_to_deck

class List_decks(ListView):
    model = Decks
    template_name = 'app_cards/List_decks.html'
    context_object_name = 'decks'

class Deck(ListView):
    model = Cards
    template_name = 'app_cards/cards_list.html'
    context_object_name = 'cards'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related().filter(link_to_deck = self.kwargs['deck_number'])
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck_number'] = self.kwargs['deck_number']
        return context

class Deck_test(ListView):
    model = Cards
    template_name = 'app_cards/cards_list_test.html'
    context_object_name = 'cards'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related().filter(link_to_deck=self.kwargs['deck_number'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck_number'] = self.kwargs['deck_number']
        return context



class Card(DetailView):
    model = Cards
    template_name = 'app_cards/card.html'
    context_object_name = 'card'

# class Add_card(CreateView):
#     model = Cards
#     template_name = 'app_cards/add_card.html'
#     fields = ['name_card', 'content', 'link_to_deck']
#     success_url = reverse_lazy('Home_page')

class Add_card_to_deck(CreateView):
    form_class = Add_card_to_deck
    template_name = 'app_cards/add_card.html'
    success_url = reverse_lazy('Home_page')
    def form_valid(self, form):
        card = form.save()
        print(self.kwargs['deck_number'])
        card.link_to_deck.add(self.kwargs['deck_number'])
        return super().form_valid(form)


class Update_card(UpdateView):
    model = Cards
    template_name = 'app_cards/update_card.html'
    fields = ['name_card', 'content', 'link_to_deck']

