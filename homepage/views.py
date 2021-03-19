from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    response = render(request, 'index.html')
    response['CustomHeader'] = 'some value'
    return response