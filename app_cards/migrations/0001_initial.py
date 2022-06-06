# Generated by Django 4.0.4 on 2022-06-04 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Decks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_deck', models.CharField(max_length=50)),
                ('amount_cards', models.IntegerField(default=0)),
                ('persent_studied', models.IntegerField(default=0)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cards.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_card', models.CharField(default='', max_length=200, verbose_name='название карточки')),
                ('content', models.TextField(default='', verbose_name='контент')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')),
                ('last_repetitions_date', models.DateTimeField(auto_now=True, verbose_name='дата последнего повторения')),
                ('number_repetitions', models.IntegerField(default=0)),
                ('link_to_deck', models.ManyToManyField(blank=True, to='app_cards.decks', verbose_name='Колода')),
            ],
        ),
    ]
