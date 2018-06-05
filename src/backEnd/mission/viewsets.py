from rest_framework import viewsets, filters
from .models import *
from .serializers import *


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('desc', 'title', 'techno')
class TechnoViewSet(viewsets.ModelViewSet):
    queryset = Techno.objects.all()
    serializer_class = TechnoSerializer
class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
class CalendrierViewSet(viewsets.ModelViewSet):
    queryset = Calendrier.objects.all()
    serializer_class = CalendrierSerializer
class UserLoginViewSet(viewsets.ModelViewSet):
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer
class PostulerViewSet(viewsets.ModelViewSet):
    queryset = Postuler.objects.all()
    serializer_class = PostulerSerializer
class Presta_missionViewSet(viewsets.ModelViewSet):
    queryset = Presta_mission.objects.all()
    serializer_class = Presta_missionSerializer