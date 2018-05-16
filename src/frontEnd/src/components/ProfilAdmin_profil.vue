<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <br />
      <b-nav justified tabs>
        <b-nav-item active>Profil</b-nav-item>
        <b-nav-item>Statistiques</b-nav-item>
        <b-nav-item>Mes missions</b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_missions'}">Gestion des missions</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_utilisateurs'}">Gestion des utilisateurs</router-link></b-nav-item>
      </b-nav>
      <b-container>
        <h1 class="titre">Profil Administrateur</h1>
        <hr class="style-four">
        <b-row class="text-center">
          <p class="text-center">{{s.firstname}} {{s.lastname}}</p>
          <p class="text-center">{{s.mail}}</p>
          <p class="text-center"> inscrit le {{s.creation_date}}</p>
        </b-row>
      </b-container>
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Nav from './Nav'
import Footer from './Footer'
import axios from 'axios'
export default {
  name: 'ProfilAdmin_profil',
  components: {Footer, Nav},
  data () {
    return {
      s: this.getStudent()
    }
  },
  mounted: function () {
    this.getStudent()
  },
  methods: {
    getStudent: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/etudiant/1'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.technos = response.data
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

</style>
