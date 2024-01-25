from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request,'home.html') 


def sobrejogo(request):
    return render(request,'crud/sobrejogo.html')

def instrucoes(request):
    return render(request,'crud/instrucoes.html')

def link(request):
    return render(request,'crud/link.html')
