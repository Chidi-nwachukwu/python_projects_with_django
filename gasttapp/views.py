from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "message": "Goodday Chidiebere"
    }
    return render(request, 'index.html' ,context)

def  chidi_goods(request):
     context = {
         "message": "Hey be careful"
     }
     return render(request, 'index.html' , context)