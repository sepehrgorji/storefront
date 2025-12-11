from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product,Customer,Order




def say_hello(request):
    # query_set = Customer.objects.filter(email__endswith=".com")
    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product ').order_by('-placed_at')[0:5]

    return render(request, 'hello.html', {'name':'sepehr','orders':list(query_set)})