from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h3>my name is lakhan </h3>")