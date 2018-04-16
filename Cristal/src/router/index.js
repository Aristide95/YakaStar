/* eslint-disable no-undef */
import Vue from 'vue'
import Router from 'vue-router'
import Accueil from '@/components/Accueil'
import Equipe from '@/components/Equipe'
import Fonctionnement from '@/components/Fonctionnement'
import Services from '@/components/Services'
import Contact from '@/components/Contact'
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
    }
  ]
})
