/* eslint-disable no-undef */
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
import ProfilAdminProfil from '@/components/ProfilAdmin_profil'
import ProfilAdminUtilisateurs from '@/components/ProfilAdmin_utilisateurs'
import ProfilAdminMissions from '@/components/ProfilAdmin_missions'
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
    }
  ]
})
