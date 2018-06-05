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
        <b-container>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p><strong>Prénom :</strong> {{currentStudent.firstname}}<br /></p>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p><strong>Nom :</strong> {{currentStudent.lastname}}<br /></p>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p><strong>Email :</strong> {{currentStudent.email}}<br /></p>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p class="text-center"> <strong>inscrit le</strong> {{ currentStudent.creation_date | moment("dddd Do MMMM YYYY") }}</p>
            </b-col>
          </b-row>
        </b-container>
        <b-container>
          <h2 class="titre">Horaire du bureau CRISTAL</h2>
          <hr class="style-four">
          <full-calendar :events="hours"></full-calendar>
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
                <b-col sm="4"><label>Début :</label></b-col>
                <b-col sm="8">
                  <b-form-input v-model="newCalendrier.dateb" type="datetime-local" required></b-form-input>
                </b-col>
              </b-row>
              <b-row class="my-1">
                <b-col sm="4"><label>Fin :</label></b-col>
                <b-col sm="8">
                  <b-form-input v-model="newCalendrier.datee" type="datetime-local" required></b-form-input>
                </b-col>
              </b-row>
              <div class="text-center">
                <b-button id="submit" type="submit" variant="primary">Créer</b-button>
              </div>
            </b-form>
          </b-modal>

          <b-modal id="myModal2">
            <b-row sm="12" v-for="h in this.futureHours" :key="hours" >
              <b-col sm="10">{{ h.start | moment("subtract", "2 hours", "LLL") }} - {{ h.end | moment("subtract", "2 hours", "LT") }} -- {{h.title}} </b-col>
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
import { FullCalendar } from 'vue-full-calendar'
import * as moment from 'moment'

export default {
  name: 'ProfilAdmin_profil',
  components: {FullCalendar, Footer, Nav},
  data () {
    return {
      student: [],
      hours: [],
      futureHours: [],
      currentStudent: [],
      newCalendrier: {
        'dateb': null,
        'datee': null
      },
      end: null,
      nowDay: null
    }
  },
  mounted: function () {
    this.getStudent()
    this.getHour()
    this.now()
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
          this.getCurrentStudent(response.data['user_id'])
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
    getCurrentStudent: function (userId) {
      let apirUrl = 'http://127.0.0.1:8000/api/etudiant/' + userId
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.currentStudent = response.data
          console.log(response.data)
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    now: function () {
      this.nowDay = moment(new Date())
      this.future(this.hours)
    },
    future: function (hours) {
      alert(hours[0].start)
      for (var i = 0; i < hours.length; i++) {
        console.log(hours[i].start.fromNow)
        if (hours[i].start.fromNow > 0) {
          this.futureHours.push(hours[i])
        }
      }
    },
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
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
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
        'title': this.currentStudent.firstname,
        'start': this.newCalendrier.dateb,
        'end': this.newCalendrier.datee
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
