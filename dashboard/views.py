from django.shortcuts import render
from django.http import HttpResponse

dt2 = [
          1,
          2,
          1,
          5,
          2,
          8,
          4, 
          20
        ]

#wilson esteve aqui

# Create your views here.
def index(request):
    return render(request, 'index.html', {'dt2':dt2})