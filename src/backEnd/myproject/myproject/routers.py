# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-02-04 23:08:11
# @Last Modified by:   shubhambansal
# @Last Modified time: 2018-02-04 23:25:39
from rest_framework import routers
from article.viewsets import ArticleViewSet
from mission.viewsets import MissionViewSet, EtudiantViewSet, TechnoViewSet, CalendrierViewSet

router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)
router.register(r'mission', MissionViewSet)
router.register(r'etudiant', EtudiantViewSet)
router.register(r'techno', TechnoViewSet)
router.register(r'calendrier', CalendrierViewSet)