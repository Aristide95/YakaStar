<template>
  <div class="profilPresta">
    <Nav></Nav>
    <b-container>
      <br />
      <b-nav justified tabs>
        <b-nav-item active>Profil</b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilPrestaMission'}">Mes Missions</router-link></b-nav-item>
      </b-nav>
      <b-container>
        <h1 class="titre">Profil prestataire</h1>
        <hr class="style-four">
        <b-container>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p><strong>Prénom :</strong> {{student[3].firstname}}<br /></p>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p><strong>Nom :</strong> {{student[3].lastname}}<br /></p>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p><strong>Email :</strong> {{student[3].email}}<br /></p>
            </b-col>
          </b-row>
          <b-row style="text-align: center">
            <b-col sm="12">
              <p class="text-center"> <strong>inscrit le</strong> {{ student[3].creation_date | moment("dddd Do MMMM YYYY") }}</p>
            </b-col>
          </b-row>
        </b-container>
      </b-container>
      <b-container>
        <h2 class="titre">Horaire du bureau CRISTAL</h2>
        <hr class="style-four">
        <vue-event-calendar :events="hours"></vue-event-calendar>
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
  name: 'ProfilPresta',
  components: {Footer, Nav},
  data () {
    return {
      student: [],
      hours: []
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
