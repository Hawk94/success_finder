from django.conf.urls import url
from .views import CustomerIndex, CustomerDetail

urlpatterns = [
    url(r'^$', CustomerIndex.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', CustomerDetail.as_view(), name='customer_detail'),
]
