from django.shortcuts import render
from django.http import HttpResponse

# Create your views heres.
def my_blog(request):
    return HttpResponse('Hello Dickson')