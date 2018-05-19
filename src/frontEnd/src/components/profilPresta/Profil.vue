<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <br />
      <b-nav justified tabs>
        <b-nav-item active>Profil</b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_statistique'}">Statistiques</router-link></b-nav-item>
        <b-nav-item>Mes missions</b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_missions'}">Gestion des missions</router-link></b-nav-item>
      </b-nav>
      <b-container>
        <h1 class="titre">Profil Administrateur</h1>
        <hr class="style-four">
        <b-container v-for="s in student" :key="s.id">
          <b-row style="text-align: center" >
            <b-col sm="3" offset="9">
              <b-btn type="button" class="btn-success" data-toggle="modal" data-target="#editMissionModal"><i class="fas fa-edit"></i></b-btn>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p><strong>Prénom :</strong> {{s.firstname}}<br /></p>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p><strong>Nom :</strong> {{s.lastname}}<br /></p>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p><strong>Email :</strong> {{s.email}}<br /></p>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p class="text-center"> <strong>inscrit le</strong> {{ s.creation_date | moment("dddd Do MMMM YYYY") }}</p>
            </b-col>
          </b-row>
        </b-container>
      </b-container>
      <b-container>
        <h2 class="titre">Horaire du bureau CRISTAL</h2>
        <hr class="style-four">
        <vue-event-calendar :title="title" :events="demoEvents"></vue-event-calendar>
      </b-container>
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Nav from '../Nav'
import Footer from '../Footer'
import axios from 'axios'
export default {
  name: 'Profil',
  components: {Footer, Nav},
  demoEvents: [],
  data () {
    return {
      student: this.getStudent()
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
  .profil {
    height: 100vh;
  }
</style>
