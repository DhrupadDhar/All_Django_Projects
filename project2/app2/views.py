from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em> this is my second django app</em>")
def help(request):
    helpdict = {'help':'help page'}
    return render(request,'app2/help.html', context = helpdict)
