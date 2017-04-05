from django.utils import timezone
from .models import Contact, AccountManager, Commission, Partner, Contract
from customers.models import Customer

import datetime


contact = Contact(name='James Miller')
manager = AccountManager(contact=contact, hurdle=200000, hurdle_period=6)
partner = Partner(contact=contact)

customer = Customer(name='BHP',
                    status='ON',
                    consultant='PH',
                    project_manager='JM',
                    initial_start_date=timezone.now() - datetime.timedelta(days=15))

commission = Commission(rate=15, discount=45)

contract = Contract(is_customer_success=True, 
                    renewable_income=2000,
                    non_renewable_income=4000,
                    currency='GBP',
                    start_date=timezone.now() - datetime.timedelta(days=15),
                    renewal_date=timezone.now(),
                    termination_clause='OM',
                    term=datetime.timedelta(days=100),
                    plants=5,
                    catalogues=5,
                    banding=3,
                    languages='EN',
                    is_active=True,
                    customer=customer,
                    partner=partner,
                    account_manager=manager,
                    key_user=contact,
                    project_sponsor=contact,
                    executive_contact=contact,
                    partner_commission=commission,
                    account_manager_commission=commission)

contact.save()
manager.save()
partner.save()
customer.save()
commission.save()
contract.save()
