from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def members(request):
    # return HttpResponse("Hello World!")
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())