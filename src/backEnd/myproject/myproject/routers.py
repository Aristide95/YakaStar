from rest_framework import routers
from mission.viewsets import MissionViewSet, EtudiantViewSet, TechnoViewSet, CalendrierViewSet

router = routers.DefaultRouter()

router.register(r'mission', MissionViewSet)
router.register(r'etudiant', EtudiantViewSet)
router.register(r'techno', TechnoViewSet)
router.register(r'calendrier', CalendrierViewSet)