from .models import Cards, Categories, Decks
#удаление карточек вынесено в отдельную функцию, так как связь между карточкой и колодой реализована, как многие ко многим
def Create_category_decks_cards_test(user_id): #функция автоматически создающая категорию с двумя колодами
    name_test_category = 'Тестовая категория'
    Categories.objects.create(name_category=name_test_category, id_user_id=user_id).save()
    deck_1 = Decks.objects.create(name_deck='колода 1', id_user_id=user_id,id_category_id=Categories.objects.get(name_category=name_test_category).id)
    deck_1.save()
    deck_2 = Decks.objects.create(name_deck='колода 2', id_user_id=user_id,id_category_id=Categories.objects.get(name_category=name_test_category).id)
    deck_2.save()
    card = Cards.objects.create(name_card='Карточка 1', content='Текст карточки 1', id_user_id=user_id)
    card.link_to_deck.add(deck_1)
    card.save()
    card = Cards.objects.create(name_card='Карточка 2', content='Текст карточки 2', id_user_id=user_id)
    card.link_to_deck.add(deck_1)
    card.save()
    card = Cards.objects.create(name_card='Карточка 3', content='Текст карточки 3', id_user_id=user_id)
    card.link_to_deck.add(deck_2)
    card.save()
    card = Cards.objects.create(name_card='Карточка 4', content='Текст карточки 4', id_user_id=user_id)
    card.link_to_deck.add(deck_2)
    card.save()

def Delete_cards_from_deck(user_id, deck_id):
    cards_for_delete = Cards.objects.filter(link_to_deck=deck_id)
    for card in cards_for_delete:
        card.delete()

def Delete_cards_from_category(user_id, category_id):
    decks_for_delete = Decks.objects.filter( id_category=category_id)
    print('////////////////////////////////////////////////////////////////')
    for dec in decks_for_delete:
        Delete_cards_from_deck(user_id, dec.id)

