<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <br />
      <b-nav justified tabs>
        <b-nav-item active>Profil</b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_statistique'}">Statistiques</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_mesMission'}">Mes missions</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_missions'}">Gestion des missions</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_utilisateurs'}">Gestion des utilisateurs</router-link></b-nav-item>
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
        <b-container>
          <h2 class="titre">Horaire du bureau CRISTAL</h2>
          <hr class="style-four">
          <vue-event-calendar :events="hours"></vue-event-calendar>
        </b-container>
        <br />
        <b-container>
          <div class="text-center">
            <b-btn class="btn-creation" v-b-modal="'myModal'">Ajouter des nouveaux horaires</b-btn>
            <b-btn class="btn-danger" v-b-modal="'myModal2'">Supprimer un horaire</b-btn>
          </div>

          <b-modal id="myModal">
            <b-form v-on:submit.prevent="addDate()">
              <b-row class="my-1">
                <b-col sm="4"><label>Date :</label></b-col>
                <b-col sm="8"><b-form-input v-model="newCalendrier.date" type="date" required></b-form-input></b-col>
              </b-row>
              <b-row class="my-1">
                <b-col sm="4"><label>Heure début :</label></b-col>
                <b-col sm="3"><b-form-input v-model="h1" type="number" min=0 max=23 required></b-form-input></b-col>
                <b-col sm="2"><div style="text-align: center">h</div></b-col>
                <b-col sm="3"><b-form-input v-model="m1" type="number" min=0 max=59 value="00"></b-form-input></b-col>
              </b-row>
              <b-row class="my-1">
                <b-col sm="4"><label>Heure fin :</label></b-col>
                <b-col sm="3"><b-form-input v-model="h2" type="number" min=0 max="23" required></b-form-input></b-col>
                <b-col sm="2"><p style="text-align: center">h</p></b-col>
                <b-col sm="3"><b-form-input v-model="m2" type="number" min=0 max="59" value="00"></b-form-input></b-col>
              </b-row>
              <div class="text-center">
                <b-button id="submit" type="submit" variant="primary">Créer</b-button>
              </div>
            </b-form>
          </b-modal>

          <b-modal id="myModal2">
            <b-row sm="12" v-for="h in this.hours" :key="hours">
              <b-col sm="10">{{ h.date | moment("dddd Do MMMM YYYY") }} -- {{h.title}} </b-col>
              <b-col sm="2"><b-btn class="btn-danger" v-on:click="deleteDate(h.id)"><i class="fas fa-times"></i></b-btn></b-col>
            </b-row>
          </b-modal>
        </b-container>
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
  name: 'ProfilAdmin_profil',
  components: {Footer, Nav},
  data () {
    return {
      student: [],
      hours: [],
      h1: '',
      m1: '',
      h2: '',
      m2: '',
      newCalendrier: {
        'date': null,
        'desc': ''
      }
    }
  },
  mounted: function () {
    this.getStudent()
    this.getHour()
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
    },
    getHour: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/calendrier/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.hours = response.data
          this.loading = false
          this.formatDate(this.hours)
          this.fillArray(this.hours)
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    formatDate: function (arrayDate) {
      for (var i = 0; i < arrayDate.length; i++) {
        var date = arrayDate[i].date
        console.log(date)
        if (date !== null) {
          arrayDate[i].date = date.replace(/-/g, '/')
        } else if (date === null) {
          arrayDate[i].date = ''
        }
      }
    },
    deleteDate: function (id) {
      let apirUrl = `http://127.0.0.1:8000/api/calendrier/${id}/`
      this.loading = true
      axios.delete(apirUrl)
        .then((response) => {
          this.loading = false
          this.getHour()
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    addDate: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/calendrier/'
      this.loading = true
      var newCal = {
        'date': this.newCalendrier.date,
        'title': this.h1.concat('h').concat(this.m1).concat(' - ').concat(this.h2).concat('h').concat(this.m2)
      }
      axios.post(apirUrl, newCal)
      .then((response) => {
        this.getHour()
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
  .btn-creation {
    background-color: #79b249;
    border-color: #598236;
  }
</style>
