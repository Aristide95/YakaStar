from rest_framework import routers
from mission.viewsets import MissionViewSet, UserLoginViewSet, EtudiantViewSet, TechnoViewSet, CalendrierViewSet, PostulerViewSet, Presta_missionViewSet

router = routers.DefaultRouter()

router.register(r'mission', MissionViewSet)
router.register(r'etudiant', EtudiantViewSet)
router.register(r'techno', TechnoViewSet)
router.register(r'calendrier', CalendrierViewSet)
router.register(r'postuler', PostulerViewSet)
router.register(r'presta_mission', Presta_missionViewSet)
router.register(r'UserLogin', UserLoginViewSet)