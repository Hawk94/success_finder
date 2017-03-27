from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ZooPage.as_view(), name='zoo_index'),
    url(r'cages', views.cage_page, name='cage_index'),
    url(r'animals', views.animal_page, name='animal_index'),
    url(r'^cage/(?P<pk>[0-9]+)/$', views.CageDetailView.as_view(), name='cage_detail'),

]