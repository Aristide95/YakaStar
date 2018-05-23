from rest_framework import serializers
from .models import *


class TechnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techno
        fields = '__all__'

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'
class CalendrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendrier
        fields = '__all__'

class MissionSerializer(serializers.ModelSerializer):
    techno =  TechnoSerializer
    commercial_id = EtudiantSerializer
    class Meta:
        model = Mission
        fields = ('__all__')




