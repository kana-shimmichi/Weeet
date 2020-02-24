from django.shortcuts import render
from django.views import generic
from home.models import Order


class Menu(generic.TemplateView):
    template_name = 'my_page/my_menu.html'

class Favorite(generic.TemplateView):
    template_name = 'my_page/favorite.html'

class Message(generic.TemplateView):
    template_name = 'my_page/message.html'

class Tradelist(generic.TemplateView):
    template_name = 'my_page/trade_list.html'


class Order(generic.CreateView):
    pass