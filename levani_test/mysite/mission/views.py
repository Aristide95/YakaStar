from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
   #add_mission(request, None)
   return HttpResponse("Hello, world. You're at the mission index.")

def add_mission_old(request, mission_dict):
   m = Mission()
   m.title = "Test"
   m.desc = "Super desc"
   m.type_mission = "my mission type"
   m.state = "My state"
   m.commercial_id = Etudiant.objects.get(pk=1)
   m.client_name = "le client"
   m.logo_url = "coucou.org"
   m.devis_url = "lol.org"
   m.save()
   m.techno.add(Techno.objects.get(pk=1))

def add_mission(request):
    print("add")
    if (request.method == 'POST'):
        form = MissionForm(request.POST)
        if (form.is_valid()):
            form.save()
            print("save")
    form = MissionForm()
    return render(request, 'base.html', {'form': form})

def delete_mission(request, mission_id):
    print("delete")
    q = get_object_or_404(Mission, pk=mission_id)
    q.delete()
    return add_mission(request)