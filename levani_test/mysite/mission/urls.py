from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_mission$', views.add_mission, name='add_mission'),
]