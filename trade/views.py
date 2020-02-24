from django.shortcuts import render
from django.views import generic


class Request(generic.TemplateView):
    template_name = 'trade/request.html'

class Consent(generic.TemplateView):
    template_name = 'trade/consent.html'

class Delivery(generic.TemplateView):
    template_name = 'trade/delivery.html'

class Credit(generic.TemplateView):
    template_name = 'trade/credit.html'

class Decline(generic.TemplateView):
    template_name = 'trade/decline.html'