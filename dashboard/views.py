from django.shortcuts import render
from django.http import HttpResponse
from .models import Quimica

# Create your views here.
def index(request):
    dt = []
    #dt2 = []
    values = Quimica.objects.all()
    for i in values:
        dt.append(i.valor)
        #dt2.append(i.nome)
    return render(request, 'index.html', {'dt':dt})
