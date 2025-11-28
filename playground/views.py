from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product,Customer




def say_hello(request):
    query_set = Customer.objects.filter(email__endswith=".com")