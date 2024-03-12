from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from members.models import Member

# Create your views here.
def members(request):
    # return HttpResponse("Hello World!")
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        "mymembers": mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        "mymember": mymember,
    }
    return HttpResponse(template.render(context, request))