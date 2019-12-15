from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView
) 
from driver.models import Driver,FieldNumber
from .forms import AddDriverForm, SignupForm,AddDriverFieldForm  
from  django.contrib.auth.models import User
# Create your views here.


def home(request):
    context = {}
    return render(request,"driver/home.html",context)

class DriverAddView(CreateView):
    model =Driver
    form_class= AddDriverForm
    template_name= "driver/add.html"
    success_url = "/driver/drivers/"

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        form.instance.user = user
        form.save()
        return super().form_valid(form)    


class FieldNumberAddView(CreateView):
    model =FieldNumber
    form_class= AddDriverFieldForm
    template_name= "driver/field_number/add.html"


    def get(self, request,*args, **kwargs):
        pk = self.kwargs['pk']
        driver = get_object_or_404(Driver, pk=pk)
        context = {
            'driver':driver,
            'form':self.form_class
        }
        print("Pk", pk)
        return render(request, self.template_name, context)

    def form_valid(self, form):
        driver = Driver.objects.get(user=self.request.user)
        form.instance.driver = driver
        form.save()
        redirect('/driver/{}'.format(driver.id))
        return super().form_valid(form)    

    # success_url = "/driver/drivers/"
    
    # def form_valid(self, form):
    #     driver = Driver.objects.get(user=self.request.user)
    #     form.instance.driver = driver
    #     return super().form_valid(form)
    

class DetailDriverView(DetailView):
    model = Driver
    template_name = "driver/detail.html"

    def get(self, request,*args, **kwargs):
        pk = self.kwargs['pk']
        driver = get_object_or_404(Driver, pk=pk)
        context = {
            'driver':driver
        }
        print("Pk", pk)
        return render(request,self.template_name, context)


class ListDriverView(ListView):
    model = Driver
    queryset = Driver.objects.all().order_by("date_added")
    template_name="driver/list.html"
    context_object_name="drivers"


class UserCreationView(CreateView):
    model = User
    form_class=SignupForm
    template_name = "driver/auth/signup.html"
    success_url="/login/"

    # def form_valid(self,form):
    #     usr = User.objects.create_user(
    #         username=form.instance.username,
    #         password=form.instance.pwd1,
    #         email=form.instance.email,
    #         first_name = form.instance.full_name,
    #         last_name =form.instance.full_name
    #     )
    #     return super().form_valid(form)
