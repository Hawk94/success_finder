from django.conf.urls import url
from .views import ZooPage, CagePage, AnimalPage

urlpatterns = [
    url(r'^$', ZooPage.as_view(), name='zoo'),
    url(r'^cages', CagePage.as_view(), name='cages'),
    url(r'^animals', AnimalPage.as_view(), name='animals'),
]
