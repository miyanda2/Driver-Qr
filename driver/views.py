from django.shortcuts import render, get_object_or_404
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
    form_class= AddDriverForm
    template_name= "driver/add.html"
    success_url = "/driver/drivers/"
    

class DetailDriverView(DetailView):
    model = Driver
    template_name = "driver/detail.html"

    def get(self, request,*args, **kwargs):
        pk = self.kwargs['pk']
        driver = get_object_or_404(Driver, pk=pk)
        context = {}
        print("Pk", pk)
        return render(request,self.template_name, context)


class ListDriverView(ListView):
    model = Driver
    queryset = Driver.objects.all().order_by("date_added")
    template_name="driver/list.html"
    context_object_name="drivers"