from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('excecuse me')
def second(request):
    return HttpResponse('good bye')

