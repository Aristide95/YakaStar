"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from .routers import router
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/', include(router.urls)),
    url('article', TemplateView.as_view(template_name='index.html')),
    url('mission', TemplateView.as_view(template_name='mission.html')),
    url('', TemplateView.as_view(template_name='index.html')),

]
