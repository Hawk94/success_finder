from django.conf.urls import url
<<<<<<< HEAD
from . import views


urlpatterns = [
    url(r'^$', views.ZooPage.as_view(), name='zoo_index'),
    url(r'cages', views.cage_page, name='cage_index'),
    url(r'animals', views.animal_page, name='animal_index'),
    url(r'^cage/(?P<pk>[0-9]+)/$', views.CageDetailView.as_view(), name='cage_detail'),

]
=======
from .views import ZooPage, CagePage, AnimalPage

urlpatterns = [
    url(r'^zoo$', ZooPage.as_view(), name='zoo'),
    url(r'^cage$', CagePage.as_view(), name='cage'),
    url(r'^animal$', AnimalPage.as_view(), name='animal'),
]
>>>>>>> 5b9301df6434630a9866467f25e3b4026750e4c4
