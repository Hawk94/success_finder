from django.views.generic import ListView, TemplateView
from django_tables2 import tables, SingleTableView
from .models import Customer, CustomerTable

# http://www.craigderington.me/generic-list-view-with-django-tables/

class CustomerIndex(SingleTableView):
    model = Customer
    table_class = CustomerTable

    template_name = "customer_index.html"


class CustomerDetail(TemplateView):
    model = Customer
    template_name = "customer_detail.html"


#################################################################################
#################################################################################


from django.views.generic import ListView
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django_tables2 import RequestConfig
from .models import Customer
from .tables import CustomerTable


class CustomerListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
  model = Customer
  template_name = 'customer_list.html'
  context_object_name = 'customer'
  ordering = ['id']
  group_required = u'company-user'

  def get_context_data(self, **kwargs):
    context = super(CustomerListView, self).get_context_data(**kwargs)
    context['nav_customer'] = True
    table = CustomerTable(Customer.objects.filter(self.kwargs['company']).order_by('-pk'))
    RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
    context['table'] = table
    return context