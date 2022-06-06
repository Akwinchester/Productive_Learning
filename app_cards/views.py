from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Decks, Cards
from django.urls import reverse_lazy
from .forms import Register_User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout

class List_decks(ListView):
    model = Decks
    template_name = 'app_cards/List_decks.html'
    context_object_name = 'decks'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_card'] = Cards.objects.order_by('?').first()
        return context


class Deck_gallery(ListView):
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


class Add_card_to_deck(CreateView):
    model = Cards
    template_name = 'app_cards/add_card.html'
    success_url = reverse_lazy('List_deck')
    fields = ('name_card', 'content')
    def form_valid(self, form):
        user_id = self.request.user.id
        card = form.save()
        card.link_to_deck.add(self.kwargs['deck_number'])
        card.id_user_id = user_id
        return super().form_valid(form)


class Update_card(UpdateView):
    model = Cards
    template_name = 'app_cards/update_card.html'
    fields = ['name_card', 'content', 'link_to_deck']

class Add_user(CreateView):
    form_class = Register_User
    template_name = 'app_cards/add_user.html'
    success_url = reverse_lazy('List_deck')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('List_deck')

class Login_user(LoginView):
    form_class = AuthenticationForm
    template_name = 'app_cards/login.html'
    def get_success_url(self):
        return reverse_lazy('List_deck')

def Logout_user(request):
    logout(request)
    return redirect('Login_user')

class Add_deck(CreateView):
    model = Decks
    fields = ['name_deck', 'id_category']
    template_name = 'app_cards/Add_deck.html'
    success_url = reverse_lazy('List_deck')
    def form_valid(self, form):
        user_id = self.request.user.id
        deck = form.save()
        deck.id_user_id = user_id
        return super().form_valid(form)
