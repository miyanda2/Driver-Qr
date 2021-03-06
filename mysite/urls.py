"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from driver.views import (
    home,
    DriverAddView,
    DetailDriverView,
    ListDriverView,
    UserCreationView,
    FieldNumberAddView
)
from driver.forms import LoginForm
from qr_code import urls as qr_code_urls
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('login/',auth_views.LoginView.as_view(template_name="driver/auth/login.html",form_class=LoginForm),name="login"),
    path('signup/', UserCreationView.as_view(), name="signup"),
    path('logout/',auth_views.LogoutView.as_view(template_name="driver/auth/logout.html"),name="logout"),
    path('driver/add/',DriverAddView.as_view(), name="driver_add"),
    path('driver/drivers/',ListDriverView.as_view(), name="driver_list"),
    path('driver/<int:pk>/',DetailDriverView.as_view(), name="driver_detail"),
    path('driver/<int:pk>/liscense/add/',FieldNumberAddView.as_view(), name="field_number"), 
    path('qr_code',include(qr_code_urls, namespace="qr_code"))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
