from django.conf.urls import url
from .views import ZooPage, CagePage, AnimalPage

urlpatterns = [
    url(r'^zoo$', ZooPage.as_view(), name='zoo'),
    url(r'^cage$', CagePage.as_view(), name='cage'),
    url(r'^animal$', AnimalPage.as_view(), name='animal'),
]
