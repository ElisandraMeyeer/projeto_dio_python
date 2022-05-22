from django.shortcuts import render
from django.views.generic import ListView
from.models import Custumer

class CustomerListView():
    template_name = "customer/customer_list.html"
    model = Custumer

# Create your views here.
