from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout

from .views import (
    ExampleSecretView, RegistrationCompleteView, RegistrationView,
)

urlpatterns = [
    url(regex=r'^logout/$',
        view=logout,
        name='logout',),
    url(regex=r'^secret/$',
        view=ExampleSecretView.as_view(),
        name='secret',),
    url(regex=r'^register/$',
        view=RegistrationView.as_view(),
        name='registration',),
    url(regex=r'^register/done/$',
        view=RegistrationCompleteView.as_view(),
        name='registration_complete',),
]
