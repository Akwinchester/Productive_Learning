from django.urls import path
from .views import  Card, Add_card_to_deck, Update_card, Deck_gallery, Add_user, Login_user, Logout_user, \
    Add_deck, Add_category, List_dekc_category, deltete_category, Create_test_set, Delete_deck, Delete_card

urlpatterns = [
    path('home_page/<slug:category_id>/', List_dekc_category.as_view(), name='List_deck_category'),
    path('card/<int:pk>', Card.as_view(), name='Card'),
    path('deck/<int:deck_number>/add_card', Add_card_to_deck.as_view(), name='Add_card'),
    path('card/<int:pk>/update_card', Update_card.as_view(), name='Update_card'),
    path('deck/<int:deck_number>', Deck_gallery.as_view(), name='Deck_gallery'),
    path('add_user/',Add_user.as_view(), name='Add_user'),
    path('login/', Login_user.as_view(), name='Login_user'),
    path('logout/', Logout_user, name='Logout_user'),
    path('add_deck/<slug:category_id>', Add_deck.as_view(), name='Add_deck'),
    path('add_category/', Add_category.as_view(), name='Add_category'),
    path('delete_category/<slug:category_id>', deltete_category, name='Delete_category'),
    path('test_set/', Create_test_set, name='Create_test_set'),
    path('deck_delete/<int:deck_number>/', Delete_deck, name='Delete_deck'),
    path('<int:deck_number>/card_delete/<int:card_id>', Delete_card, name='Delete_card')
]