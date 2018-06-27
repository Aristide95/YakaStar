<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <div v-if="currentStudent.status === 'admin'">
        <br />
        <b-nav justified tabs>
          <b-nav-item><router-link :to="{name: 'ProfilAdmin_profil'}">Profil</router-link></b-nav-item>
          <b-nav-item active>Statistiques</b-nav-item>
          <b-nav-item><router-link :to="{name: 'ProfilAdmin_mesMission'}">Mes missions</router-link></b-nav-item>
          <b-nav-item><router-link :to="{name: 'ProfilAdmin_missions'}">Gestion des missions</router-link></b-nav-item>
          <b-nav-item><router-link :to="{name: 'ProfilAdmin_utilisateurs'}">Gestion des utilisateurs</router-link></b-nav-item>
        </b-nav>
        <b-container>
          <h1 class="titre">Statistiques</h1>
          <hr class="style-four">
          <b-row>
            <b-col sm="4" class="center-block">
              <b-btn class="btn-info" v-on:click="createPDF()">Exporter les statistiques en format PDF</b-btn>
            </b-col>
          </b-row>
          <h3 class="titre">Total des missions : {{missions.length}}</h3>
          <b-row>
            <b-col sm="4">
              <h6 class="titre">Nombre de missions réalisées : {{termine.length}}</h6>
              <div class="pie">
                <pie-chart
                  :percent='t'
                  :stroke-width=1
                  :abel='tString'
                  label-small=""
                  color=#40a070
                  :opacity=0.7
                />
              </div>
            </b-col>
            <b-col sm="4">
              <h6 class="titre">Nombre de missions en cours : {{enCours.length}}</h6>
              <div class="pie">
                <pie-chart
                  :percent='e'
                  :stroke-width=1
                  :abel='eString'
                  label-small=""
                  color=#40a070
                  :opacity=0.7
                />
              </div>
            </b-col>
            <b-col sm="4">
              <h6 class="titre">Nombre de missions annulées : {{annule.length}}</h6>
              <div class="pie">
                <pie-chart
                  :percent='a'
                  :stroke-width=1
                  :abel='aString'
                  label-small=""
                  color=#40a070
                  :opacity=0.7
                />
              </div>
            </b-col>
          </b-row>
          <br />
          <h3 class="titre">Total des prestaires : {{student.length}}</h3>
          <b-row>
            <b-col sm="4">
              <h6 class="titre">Nombre de commerciaux : {{com.length}}</h6>
              <div class="pie">
                <pie-chart
                  :percent='c'
                  :stroke-width=1
                  :abel='cString'
                  label-small=""
                  color=#407fa0
                  :opacity=0.7
                />
              </div>
            </b-col>
            <b-col sm="4">
              <h6 class="titre">Nombre de MVP : {{mvp.length}}</h6>
              <div class="pie">
                <pie-chart
                  :percent='m'
                  :stroke-width=1
                  :abel='mString'
                  label-small=""
                  color=#407fa0
                  :opacity=0.7
                />
              </div>
            </b-col>
            <b-col sm="4">
              <h6 class="titre">Nombre de prestataire en mission : {{nbp.length}}</h6>
              <div class="pie">
                <pie-chart
                  :percent='n'
                  :stroke-width=1
                  :abel='nString'
                  label-small=""
                  color=#407fa0
                  :opacity=0.7
                />
              </div>
            </b-col>
          </b-row>
          <br />
          <h4 class="titre">Meilleurs prestataires</h4>
          <b-table striped :items="mvp" :fields="fields"></b-table>
        </b-container>
        <b-row>
          <b-col sm="4" class="center-block">
            <download-excel
              class   = "btn btn-info"
              :data   = "json_data"
              :fields = "json_fields"
              name    = "statistiques_CRISTAL.xls">
              Exporter les statistiques en format Excel
            </download-excel>
          </b-col>
        </b-row>
      </div>
      <div v-else>
        <h2 class="titre">Erreur 403 : vous n'avez pas les droits</h2>
        <div style="text-align: center">
          <img class="img-responsive img-fluid" src="../../assets/403.jpg" alt="erreur 403"/>
        </div>
        <h3 class="titre"><router-link :to="{name: 'Accueil'}">Revenir à la page d'accueil</router-link></h3>
      </div>
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
/* eslint-disable new-cap */
import Nav from '../Nav'
import Footer from '../Footer'
import axios from 'axios'
import PieChart from 'vue-pie-chart/src/PieChart.vue'
import jsPDF from 'jsPDF'
import JsonExcel from 'vue-json-excel'
export default {
  name: 'ProfilAdmin_statistique',
  components: {Footer, Nav, 'pie-chart': PieChart, 'download-excel': JsonExcel},
  data () {
    return {
      json_fields: {
        'Statistique': 'String',
        'Nombre': 'String',
        'Pourcentage': 'Number'
      },
      json_data: [],
      json_meta: [
        [{
          'key': 'charset',
          'value': 'utf-8'
        }]
      ],
      student: [],
      missions: [],
      annule: [],
      enCours: [],
      termine: [],
      currentStudent: [],
      a: 0,
      aString: '0',
      e: 0,
      eString: '0',
      t: 0,
      tString: '0',
      c: 0,
      cString: '0',
      m: 0,
      mString: '0',
      n: 0,
      nString: '0',
      nbPresta: [],
      nbp: [],
      com: [],
      mvp: [],
      eleve: [],
      fields: [
        {
          key: 'firstname',
          label: 'Prénom',
          sortable: true
        },
        {
          key: 'lastname',
          label: 'Nom',
          sortable: true
        },
        {
          key: 'email',
          sortable: false
        }
      ]
    }
  },
  mounted: function () {
    this.test()
    this.getStudent()
    this.getMissions()
    this.getPresta_mission()
    this.getExcel()
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
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    getPresta_mission: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/presta_mission/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.nbPresta = response.data
          var bool = true
          if (this.nbPresta.length !== 0) {
            this.nbp.push(this.nbPresta[0])
            for (var i = 1; i < this.nbPresta.length; i++) {
              for (var j = 0; j < this.nbp.length && bool; j++) {
                if (this.nbPresta[i].etudiant_id === this.nbp[j].etudiant_id) {
                  bool = false
                }
              }
              if (bool) {
                this.nbp.push(this.nbPresta[i])
              }
              bool = true
            }
            if (this.nbp.length !== 0) {
              this.n = this.nbp.length / this.student.length * 100
              this.nString = this.n.toString()
            }
          }
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    sortStudents: function (students) {
      for (var i = 0; i < students.length; i++) {
        if (students[i].status === 'com') {
          this.com.push(students[i])
        } else if (students[i].status === 'mvp') {
          this.mvp.push(students[i])
        } else {
          this.eleve.push(students[i])
        }
      }
      if (this.com.length !== 0) {
        this.c = this.com.length / this.student.length * 100
        this.cString = this.c.toString()
      }
      if (this.mvp.length !== 0) {
        this.m = this.mvp.length / this.student.length * 100
        this.mString = this.m.toString()
      }
    },
    getMissions: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/mission/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.missions = response.data
          this.sortMission(this.missions)
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    sortMission: function (missions) {
      for (var i = 0; i < missions.length; i++) {
        if (missions[i].state === 3) {
          this.enCours.push(missions[i])
        } else if (missions[i].state === 4) {
          this.termine.push(missions[i])
        } else if (missions[i].state === 5) {
          this.annule.push(missions[i])
        }
      }
      if (this.termine.length !== 0) {
        this.t = this.termine.length / this.missions.length * 100
        this.tString = this.t.toString()
      }
      if (this.annule.length !== 0) {
        this.a = this.annule.length / this.missions.length * 100
        this.aString = this.a.toString()
      }
      if (this.enCours.length !== 0) {
        this.e = this.enCours.length / this.missions.length * 100
        this.eString = this.e.toString()
      }
    },
    getStudent: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/etudiant/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.student = response.data
          this.sortStudents(this.student)
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    createPDF () {
      let pdfName = 'statistique_CRISTAL'
      var doc = new jsPDF()

      doc.text('STATISTIQUES', 85, 10)
      doc.text('MISSIONS', 10, 20)
      doc.text('Nombre de missions : ' + this.missions.length, 20, 30)
      doc.text('Nombre de missions réalisées : ' + this.termine.length + ' soit ' + this.t + '%', 20, 40)
      doc.text('Nombre de missions en cours : ' + this.enCours.length + ' soit ' + this.e + '%', 20, 50)
      doc.text('Nombre de missions annulées : ' + this.annule.length + ' soit ' + this.a + '%', 20, 60)

      doc.text('PRESTATAIRES', 10, 80)
      doc.text('Nombre de prestataires : ' + this.student.length, 20, 90)
      doc.text('Nombre de commerciaux : ' + this.com.length + ' soit ' + this.c + '%', 20, 100)
      doc.text('Nombre de MVP : ' + this.mvp.length + ' soit ' + this.m + '%', 20, 110)
      doc.text('Nombre de prestataire en mission : ' + this.nbPresta.length + ' soit ' + this.n + '%', 20, 120)

      doc.text('Meilleurs prestataires', 10, 140)

      for (var i = 0; i < this.mvp.length; i++) {
        doc.text(this.mvp[i].lastname, 20, 150 + i * 10)
        doc.text(this.mvp[i].firstname, 80, 150 + i * 10)
      }

      doc.save(pdfName + '.pdf')
    },
    getExcel: function () {
      this.json_data = [
        {
          'Statistique': 'Nombre de missions',
          'Nombre': this.missions.length.toString(),
          'Pourcentage': 0
        },
        {
          'Statistique': 'Nombre de missions réalisées',
          'Nombre': this.termine.length.toString(),
          'Pourcentage': this.t
        },
        {
          'Statistique': 'Nombre de missions en cours',
          'Nombre': this.enCours.length.toString(),
          'Pourcentage': this.e
        },
        {
          'Statistique': 'Nombre de missions annulées',
          'Nombre': this.annule.length.toString(),
          'Pourcentage': this.a
        },
        {
          'Statistique': 'Nombre de prestataires',
          'Nombre': this.student.length.toString(),
          'Pourcentage': 0
        },
        {
          'Statistique': 'Nombre de commerciaux',
          'Nombre': this.com.length.toString(),
          'Pourcentage': this.c
        },
        {
          'Statistique': 'Nombre de MVP',
          'Nombre': this.mvp.length.toString(),
          'Pourcentage': this.m
        },
        {
          'Statistique': 'Nombre de prestataire en mission',
          'Nombre': this.nbPresta.length.toString(),
          'Pourcentage': this.n
        }
      ]
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
  .pie {
    max-width: 50%;
    max-height: 50%;
    text-align: center;
    margin-left:auto;
    margin-right:auto;
    display:block;
  }
  .center-block {
    margin-left:auto;
    margin-right:auto;
    display:block;
  }
</style>
