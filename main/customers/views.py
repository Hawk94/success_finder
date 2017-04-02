from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView
from django_tables2 import tables, SingleTableView
from django.urls import reverse_lazy
from .models import Customer
from .tables import CustomerTable

# http://www.craigderington.me/generic-list-view-with-django-tables/

class CustomerIndex(SingleTableView):
    model = Customer
    table_class = CustomerTable
    template_name = "customer_index.html"


class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'initial_start_date']
    template_name = "customer_form.html"
    success_url = reverse_lazy('customers:index')


class CustomerDetail(DetailView):
    model = Customer
    template_name = "customer_detail.html"