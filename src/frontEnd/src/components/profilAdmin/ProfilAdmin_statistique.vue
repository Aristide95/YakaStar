<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
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
          <b-col sm="4" offset="5">
            <b-btn class="btn-info" v-on:click="createPDF()">Exporter les statistiques</b-btn>
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
            <h6 class="titre">Nombre de prestataire en mission : {{nb_presta.length}}</h6>
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
export default {
  name: 'ProfilAdmin_statistique',
  components: {Footer, Nav, 'pie-chart': PieChart},
  data () {
    return {
      student: [],
      missions: [],
      annule: [],
      enCours: [],
      termine: [],
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
      nb_presta: 0,
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
    this.getStudent()
    this.getMissions()
    this.getPresta_mission()
  },
  methods: {
    getPresta_mission: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/presta_mission/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.nb_presta = response.data
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
      if (this.nb_presta.length !== 0) {
        this.n = this.nb_presta.length / this.student.length * 100
        this.nString = this.n.toString()
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
          this.nb_presta = this.nb_presta + missions[i].nb_presta
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
      doc.text('Nombre de prestataire en mission : ' + this.nb_presta.length + ' soit ' + this.n + '%', 20, 120)

      doc.text('Meilleurs prestataires', 10, 140)

      for (var i = 0; i < this.mvp.length; i++) {
        doc.text(this.mvp[i].lastname, 20, 150 + i * 10)
        doc.text(this.mvp[i].firstname, 80, 150 + i * 10)
      }

      doc.save(pdfName + '.pdf')
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
</style>
