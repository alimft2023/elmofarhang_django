from django.shortcuts import render
from .models import Todo

# Create your views here.
def hello(request):
    x=Todo.objects.get(id=1)
    return render(request,'hello.html',{'y':x})