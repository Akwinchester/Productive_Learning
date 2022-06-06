from django.urls import path
from .views import List_decks, Card, Add_card_to_deck, Update_card, Deck_gallery, Add_user, Login_user, Logout_user, Add_deck

urlpatterns = [
    path('home_page/', List_decks.as_view(), name='List_deck'),
    path('card/<int:pk>', Card.as_view(), name='Card'),
    path('deck/<int:deck_number>/add_card', Add_card_to_deck.as_view(), name='Add_card'),
    path('card/<int:pk>/update_card', Update_card.as_view(), name='Update_card'),
    path('deck/<int:deck_number>/gallery', Deck_gallery.as_view(), name='Deck_gallery'),
    path('add_user/',Add_user.as_view(), name='Add_user'),
    path('login/', Login_user.as_view(), name='Login_user'),
    path('logout/', Logout_user, name='Logout_user'),
    path('add_deck/', Add_deck.as_view(), name='Add_deck'),
]