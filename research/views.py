from django.shortcuts import render
from django.views import generic


class Contractor_form(generic.TemplateView):
    template_name = 'research/contractor_form.html'

class Contractor_result(generic.TemplateView):
    template_name = 'research/contractor_result.html'

class Orderer_form(generic.TemplateView):
    template_name = 'research/orderer_form.html'

class Orderer_result(generic.TemplateView):
    template_name = 'research/orderer_result.html'
