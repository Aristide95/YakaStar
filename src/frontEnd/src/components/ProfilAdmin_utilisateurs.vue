<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <br />
      <b-nav justified tabs>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_profil'}">Profil</router-link></b-nav-item>
        <b-nav-item>Statistiques</b-nav-item>
        <b-nav-item> Mes missions</b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_missions'}">Gestion des missions</router-link></b-nav-item>
        <b-nav-item active>Gestion des utilisateurs</b-nav-item>
        <b-container>
          <h1 class="titre">Utilisateurs</h1>
          <hr class="style-four">
          <b-table striped hover :items="students" :fields="fields"></b-table>
        </b-container>
      </b-nav>
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
      students: this.getStudent(),
      fields: [ 'firstname', 'lastname', 'email', 'status' ],
      loading: false
    }
  },
  mounted: function () {
    this.getStudent()
  },
  methods: {
    getStudent: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/etudiant/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.students = response.data
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
  hr.style-four {
    height: 12px;
    border: 0;
    box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);
  }
  .titre{
    color: #0c365a;
    text-align: center;
    padding-top: 30px;
    padding-bottom: 20px;
  }
</style>
