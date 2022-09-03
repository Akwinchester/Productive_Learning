from django.urls import path
from .views import   AddСardToDeck, UpdateCard, CardsByDeck, AddUser, LoginUser, logout_user, \
    AddDeck, AddCategory, DeckByCategory, deltete_category, create_test_set, delete_deck, delete_card

urlpatterns = [
    path('home_page/<slug:category_id>/', DeckByCategory.as_view(), name='List_deck_category'),
    path('deck/<int:deck_number>/add_card', AddСardToDeck.as_view(), name='Add_card'),
    path('card/<int:pk>/update_card', UpdateCard.as_view(), name='Update_card'),
    path('deck/<int:deck_number>', CardsByDeck.as_view(), name='Deck_gallery'),
    path('add_user/', AddUser.as_view(), name='Add_user'),
    path('login/', LoginUser.as_view(), name='Login_user'),
    path('logout/', logout_user, name='Logout_user'),
    path('add_deck/<slug:category_id>', AddDeck.as_view(), name='Add_deck'),
    path('add_category/', AddCategory.as_view(), name='Add_category'),
    path('delete_category/<slug:category_id>', deltete_category, name='Delete_category'),
    path('test_set/', create_test_set, name='Create_test_set'),
    path('deck_delete/<int:deck_number>/', delete_deck, name='Delete_deck'),
    path('<int:deck_number>/card_delete/<int:card_id>', delete_card, name='Delete_card')
]