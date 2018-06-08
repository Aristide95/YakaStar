<template>
  <div id="nav">
    <div id="fixe">
      <b-container fluid>
        <b-navbar toggleable="md">

          <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

          <b-navbar-brand href="#"><router-link :to="{name: 'Accueil'}">
            <img class="logo" src="../assets/logo.png" alt="Logo Cristal" />
          </router-link></b-navbar-brand>
          <b-container>
            <b-collapse is-nav id="nav_collapse">

              <b-navbar-nav>
                <b-nav-item href="#"><router-link :to="{name: 'Accueil'}">Accueil</router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{name: 'Equipe'}">Équipe</router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{name: 'Services'}">Services</router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{name: 'Fonctionnement'}">Fonctionnement</router-link></b-nav-item>
                <b-nav-item href="#" v-if="student.length !== 0"><router-link :to="{name: 'Missions'}">Missions</router-link></b-nav-item>
              </b-navbar-nav>

              <!-- Right aligned nav items -->
              <b-navbar-nav class="ml-auto">
                <b-nav-item right v-if="student.length === 0" href="http://127.0.0.1:8000/login/epita/">Connexion</b-nav-item>
                <b-nav-item right v-if="student.length !== 0 && student.status === 'admin'"><router-link :to="{name: 'ProfilAdmin_profil'}">{{student.firstname}}</router-link></b-nav-item>
                <b-nav-item right v-else-if="student.length !== 0 && student.status === 'commercial'"><router-link :to="{name: 'Profil'}">{{student.firstname}}</router-link></b-nav-item>
                <b-nav-item right v-else><router-link :to="{name: 'ProfilPresta'}">{{student.firstname}}</router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{name: 'Contact'}">Contact</router-link></b-nav-item>
                <b-nav-item href="http://localhost:8080/#/" v-if="student.length !== 0"><i class="fas fa-sign-out-alt"></i></b-nav-item>
              </b-navbar-nav>

            </b-collapse>
          </b-container>
        </b-navbar>
      </b-container>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Nav',
  show: true,
  data () {
    return {
      student: []
    }
  },
  mounted: function () {
    this.test()
  },
  methods: {
    test: function () {
      let data = new FormData()
      var tokenFromCookie = this.getCookie('access_token')
      data.set('access_token', tokenFromCookie)
      let apirUrl = `http://127.0.0.1:8000/islogged/`
      axios({
        method: 'post',
        url: apirUrl,
        data: data,
        config: {headers: { 'Content-Type': 'multipart/form-data' }}
      })
        .then((response) => {
          this.getStudent(response.data['user_id'])
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getCookie: function (name) {
      var cookie = name + '='
      var ca = document.cookie.split(';')
      for (var i = 0; i < ca.length; i++) {
        var c = ca[i]
        while (c.charAt(0) === ' ') c = c.substring(1)
        if (c.indexOf(cookie) === 0) return c.substring(cookie.length, c.length)
      }
      return ''
    },
    getStudent: function (userId) {
      let apirUrl = 'http://127.0.0.1:8000/api/etudiant/' + userId
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.student = response.data
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  .logo{
    max-width: 125px;
    height: auto;
  }
  #fixe {
    overflow: hidden;
    position: fixed;
    top: 0;
    width: 100%;
    background-color: white;
    z-index: 100;
  }
  #nav {
    padding-bottom: 80px;
  }
  a {
    text-decoration: none;
    color: rgba(0, 0, 0, 0.5);
  }
  a:hover, a:focus {
    color: #0c365a;
  }
  a:active {
    color: #79b249;
  }
</style>
