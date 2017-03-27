from django.views import generic
<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils import timezone

from .models import Cage, BaseAnimal
from .tables import CageTable


class HomePage(generic.TemplateView):
    template_name = "home.html"\


class ZooPage(generic.TemplateView):
    template_name = "zoo_index.html"

# def zoo_index(request, template_name='zoo_index.html'):
#     return render(request, template_name)


def cage_page(request):
    template = "cage_index.html"
    query_results = Cage.objects.all()
    table = CageTable(query_results)

    return render(request, template, {'table': table})


def animal_page(request):
    template = "animal_index.html"
    query_results = BaseAnimal.objects.all()
    table = CageTable(query_results)

    return render(request, template, {'table': table})


class CageDetailView(generic.DetailView):

    model = Cage
    template_name = "cage_detail.html"
=======


class ZooPage(generic.TemplateView):
    template_name = "zoo.html"


class CagePage(generic.TemplateView):
    template_name = "cage.html"


class AnimalPage(generic.TemplateView):
    template_name = "animal.html"
>>>>>>> 5b9301df6434630a9866467f25e3b4026750e4c4
