import Vue from 'vue'
import Router from 'vue-router'
import Accueil from '@/components/Accueil'
import Equipe from '@/components/Equipe'
import Fonctionnement from '@/components/Fonctionnement'
import Services from '@/components/Services'
import Contact from '@/components/Contact'
import Faq from '@/components/Faq'
import Missions from '@/components/Missions'
import Connexion from '@/components/Connexion'
import ProfilAdminProfil from '@/components/profilAdmin/ProfilAdmin_profil'
import ProfilAdminUtilisateurs from '@/components/profilAdmin/ProfilAdmin_utilisateurs'
import ProfilAdminMissions from '@/components/profilAdmin/ProfilAdmin_missions'
import ProfilAdminStat from '@/components/profilAdmin/ProfilAdmin_statistique'
import ProfilPresta from '@/components/profilPresta/ProfilPresta'
import ProfilPrestaMission from '@/components/profilPresta/ProfilPrestaMission'
import ProfilCom from '@/components/profilCom/Profil'
import ProfilComMission from '@/components/profilCom/ProfilCom_missions'
import ProfilComStat from '@/components/profilCom/ProfilCom_statistique'
import CreationMission from '@/components/CreationMission'
import VueCarousel from 'vue-carousel'
Vue.use(VueCarousel)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Accueil',
      component: Accueil
    },
    {
      path: '/equipe',
      name: 'Equipe',
      component: Equipe
    },
    {
      path: '/fonctionnement',
      name: 'Fonctionnement',
      component: Fonctionnement
    },
    {
      path: '/services',
      name: 'Services',
      component: Services
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact
    },
    {
      path: '/faq',
      name: 'Faq',
      component: Faq
    },
    {
      path: '/creation-mission',
      name: 'creation-mission',
      component: CreationMission
    },
    {
      path: '/missions',
      name: 'Missions',
      component: Missions
    },
    {
      path: '/connexion',
      name: 'Connexion',
      component: Connexion
    },
    {
      path: '/profil/admin/',
      name: 'ProfilAdmin_profil',
      component: ProfilAdminProfil
    },
    {
      path: '/profil/admin/utilisateurs',
      name: 'ProfilAdmin_utilisateurs',
      component: ProfilAdminUtilisateurs
    },
    {
      path: '/profil/admin/missions',
      name: 'ProfilAdmin_missions',
      component: ProfilAdminMissions
    },
    {
      path: '/profil/admin/statistiques',
      name: 'ProfilAdmin_statistique',
      component: ProfilAdminStat
    },
    {
      path: '/profil/prestataire/',
      name: 'ProfilPresta',
      component: ProfilPresta
    },
    {
      path: '/profil/prestataire/missions',
      name: 'ProfilPrestaMission',
      component: ProfilPrestaMission
    },
    {
      path: '/profil/commercial/',
      name: 'ProfilCom',
      component: ProfilCom
    },
    {
      path: '/profil/commercial/missions',
      name: 'ProfilComMission',
      component: ProfilComMission
    },
    {
      path: '/profil/commercial/statistique',
      name: 'ProfilComStat',
      component: ProfilComStat
    }
  ]
})
