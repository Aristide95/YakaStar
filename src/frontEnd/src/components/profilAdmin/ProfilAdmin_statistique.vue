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
        <h3 class="titre">Total des missions : {{missions.length}}</h3>
        <b-row>
          <b-col sm="4">
            <h6 class="titre">Nombre de mission réalisée : {{termine.length}}</h6>
            <div class="pie">
              <pie-chart
                :percent='t'
                :stroke-width=1
                :label='t'
                label-small=""
                color=#40a070
                :opacity=0.7
              />
            </div>
          </b-col>
          <b-col sm="4">
            <h6 class="titre">Nombre de mission en cours : {{enCours.length}}</h6>
            <div class="pie">
              <pie-chart
                :percent='e'
                :stroke-width=1
                :label='e'
                label-small=""
                color=#40a070
                :opacity=0.7
              />
            </div>
          </b-col>
          <b-col sm="4">
            <h6 class="titre">Nombre de mission annulée : {{annule.length}}</h6>
            <div class="pie">
              <pie-chart
                :percent='a'
                :stroke-width=1
                :abel='a'
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
                :label='c'
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
                :label='m'
                label-small=""
                color=#407fa0
                :opacity=0.7
              />
            </div>
          </b-col>
          <b-col sm="4">
            <h6 class="titre">Nombre de prestataire en mission: {{nb_presta}}</h6>
            <div class="pie">
              <pie-chart
                :percent='n'
                :stroke-width=1
                :abel='n'
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
import Nav from '../Nav'
import Footer from '../Footer'
import axios from 'axios'
import PieChart from 'vue-pie-chart/src/PieChart.vue'
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
      a: 25,
      e: 0,
      t: 0,
      c: 28,
      m: 14,
      n: 0,
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
  },
  methods: {
    calcul: function () {
      if (this.termine.length !== 0) {
        this.t = this.termine.length / this.missions.length * 100
      }
      if (this.annule.length !== 0) {
        this.a = this.annule.length / this.missions.length * 100
      }
      if (this.enCours.length !== 0) {
        this.e = this.enCours.length / this.missions.length * 100
      }
      if (this.com.length !== 0) {
        this.c = this.com.length / this.student.length * 100
      }
      if (this.mvp.length !== 0) {
        this.m = this.mvp.length / this.student.length * 100
      }
      if (this.nb_presta !== 0) {
        this.n = this.nb_presta / this.student.length * 100
      }
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
    },
    getMissions: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/mission/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.missions = response.data
          this.sortMission(this.missions)
          this.calcul()
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    sortMission: function (missions) {
      for (var i = 0; i < missions.length; i++) {
        if (missions[i].state === 2) {
          this.pourvue.push(missions[i])
        } else if (missions[i].state === 3) {
          this.enCours.push(missions[i])
          this.nb_presta = this.nb_presta + missions[i].nb_presta
        } else if (missions[i].state === 4) {
          this.termine.push(missions[i])
        } else if (missions[i].state === 5) {
          this.annule.push(missions[i])
        }
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
