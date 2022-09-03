from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Decks, Cards, Categories
from django.urls import reverse_lazy
from .forms import Register_User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from .services import Delete_cards_from_category, Create_category_decks_cards_test, Delete_cards_from_deck


class DeckByCategory(ListView):
    model = Decks
    template_name = 'app_cards/List_decks_category.html'
    context_object_name = 'decks'
    def get_queryset(self):
        qs = super().get_queryset()
        if self.kwargs['category_id'] == 'all':
            return qs.filter(id_user_id = self.request.user.id)
        return qs.filter(id_category = self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs['category_id']
        if self.kwargs['category_id'] != 'all':
            context['category_id_int'] = int(self.kwargs['category_id'])
        else:
            context['category_id_int'] = -1
        context['random_card'] = Cards.objects.order_by('?').first()
        context['categories'] = Categories.objects.filter(id_user_id=self.request.user.id)

        if self.kwargs['category_id'] != 'all':
            context['name_used_category'] = Categories.objects.get(id=self.kwargs['category_id'])

        context['id_generic_category'] = Categories.objects.filter(id_user_id=self.request.user.id).get(name_category='Общая').id
        return context


class CardsByDeck(ListView):
    model = Cards
    template_name = 'app_cards/deck_gallery.html'
    context_object_name = 'cards'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related().filter(link_to_deck=self.kwargs['deck_number'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck_number'] = self.kwargs['deck_number']
        context['deck'] = Decks.objects.get(id=self.kwargs['deck_number'])
        return context


class AddСardToDeck(CreateView):
    model = Cards
    template_name = 'app_cards/add_card.html'
    # success_url = reverse_lazy('List_deck_category', args=[deck_number])
    fields = ('name_card', 'content')
    def get_success_url(self):
        return reverse_lazy('Deck_gallery', args=[self.kwargs['deck_number']])
    def form_valid(self, form):
        user_id = self.request.user.id
        card = form.save(commit=False)
        card.id_user_id = user_id
        card = form.save()
        card.link_to_deck.add(self.kwargs['deck_number'])
        return super().form_valid(form)


class UpdateCard(UpdateView):
    model = Cards
    template_name = 'app_cards/update_card.html'
    fields = ['name_card', 'content']
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(id_user_id=self.request.user.id)


class AddUser(CreateView):
    form_class = Register_User
    template_name = 'app_cards/add_user.html'
    success_url = reverse_lazy('List_deck_category', args = ['all'])
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        general_category = Categories.objects.create(name_category='Общая', id_user_id=self.request.user.id)
        general_category.save()
        return redirect(reverse_lazy('List_deck_category', args=['all']))


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'app_cards/login.html'
    def get_success_url(self):
        return reverse_lazy('List_deck_category', args = ['all'])


class AddDeck(CreateView):
    model = Decks
    fields = ['name_deck', 'id_category']
    template_name = 'app_cards/add_deck.html'
    success_url = reverse_lazy('List_deck_category', args = ['all'])
    def form_valid(self, form):
        user_id = self.request.user.id
        deck = form.save(commit=False)
        deck.id_user_id = user_id
        if self.kwargs['category_id'] == 'all':
            deck.id_category_id = Categories.objects.get(id_user_id=self.request.user.id).id
        else:
            deck.id_category_id = self.kwargs['category_id']
        return super().form_valid(form)


class AddCategory(CreateView):
    model = Categories
    fields = ['name_category',]
    template_name = 'app_cards/add_category.html'
    success_url = reverse_lazy('List_deck_category', args = ['all'])
    def form_valid(self, form):
        user_id = self.request.user.id
        category = form.save(commit=False)
        category.id_user_id = user_id
        return super().form_valid(form)


def deltete_category(request, category_id):
    category = Categories.objects.get(id=category_id)
    Delete_cards_from_category(user_id=request.user.id, category_id=category_id)
    category.delete()
    return redirect(reverse_lazy('List_deck_category', args=['all']))


def delete_deck(request, deck_number):
    deck = Decks.objects.get(id=deck_number)
    category_id = deck.id_category_id
    Delete_cards_from_deck(request.user.id, deck_number)
    deck.delete()
    return redirect(reverse_lazy('List_deck_category', args=[category_id]))


def delete_card(request, card_id, deck_number):
    card = Cards.objects.get(id=card_id)
    card.delete()
    return redirect(reverse_lazy('Deck_gallery', args=[deck_number]))


def logout_user(request):
    logout(request)
    return redirect('Login_user')


def create_test_set(request):
    Create_category_decks_cards_test(request.user.id)
    return  redirect(reverse_lazy('List_deck_category', args=['all']))