from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView
) 
from driver.models import Driver
from .forms import AddDriverForm  
# Create your views here.


def home(request):
    context = {}
    return render(request,"driver/home.html",context)

class DriverAddView(CreateView):
    model =Driver
    form_class= AddDriverForm()
    template_name= "driver/add.html"
    

class DetailDriverView(DetailView):
    model = Driver
    template_name = "driver/detail.html"

class ListDriverView(ListView):
    model = Driver
    queryset = Driver.objects.all()
    template_name="driver/list.html"