from django.views import generic


class ZooPage(generic.TemplateView):
    template_name = "zoo.html"


class CagePage(generic.TemplateView):
    template_name = "cage.html"


class AnimalPage(generic.TemplateView):
    template_name = "animal.html"