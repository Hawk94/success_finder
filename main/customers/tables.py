import django_tables2 as tables
from django_tables2.utils import A
from .models import Customer


class CustomerTable(tables.Table):
    customer_name = tables.LinkColumn('customer-detail', args=[A('pk')])
    
    class Meta:
        model = Customer
        fields = ('name')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no customers matching the search criteria..."