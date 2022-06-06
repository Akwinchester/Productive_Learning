from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
class Categories(models.Model):
    name_category =models.CharField(max_length=100, default='')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_category

class Decks(models.Model):
    name_deck = models.CharField(max_length=50, verbose_name='Название')
    amount_cards = models.IntegerField(default=0)
    persent_studied = models.IntegerField(default=0)
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория',default=1)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name_deck

class Cards(models.Model):
    name_card = models.CharField(max_length=200, default='', verbose_name="название карточки")
    content = models.TextField(default='', verbose_name='контент')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    last_repetitions_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего повторения')
    number_repetitions = models.IntegerField(default=0)
    link_to_deck = models.ManyToManyField(Decks, verbose_name='Колода',blank=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def get_absolute_url(self):
        return reverse('Card', kwargs={'pk': self.id})
    def __str__(self):
        return self.name_card

