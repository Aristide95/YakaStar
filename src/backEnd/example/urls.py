from django.conf.urls import url

from .views import home, logged, islogged
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^logged/$', logged, name='logged'),
    url(r'^islogged/$', islogged, name='islogged'),
]
