from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
    # Wrok with daatbase
    # Transform data
    # Data pass
    # Http resonse / json response

def home(request):
   return HttpResponse("Weclome to task manegement projetc")

def contact(request):
   return HttpResponse("<h1 style = 'color:blue'>This is contact page<h1>")

def showTasks(resposne):
   return HttpResponse("You are in show-tasks page")