<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <br />
      <b-nav justified tabs>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_profil'}">Profil</router-link></b-nav-item>
        <b-nav-item active>Statistiques</b-nav-item>
        <b-nav-item>Mes missions</b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_missions'}">Gestion des missions</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_utilisateurs'}">Gestion des utilisateurs</router-link></b-nav-item>
      </b-nav>
      <b-container>
        <h1 class="titre">Statistiques</h1>
        <hr class="style-four">
        <Pie :data="this.data1"
             :options="this.options"></Pie>
      </b-container>
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Nav from '../Nav'
import Footer from '../Footer'
import axios from 'axios'
import Pie from 'vue-chartjs/es/BaseCharts/Pie'
export default {
  export: Pie,
  name: 'ProfilAdmin_statistique',
  components: {Pie, Footer, Nav},
  data () {
    return {
      student: this.getStudent(),
      data1: {
        labels: ['match1', 'match2', 'match3', 'match4', 'match5'],
        datasets: [
          {
            label: 'TeamA Score',
            data: [10, 50, 25, 70, 40],
            backgroundColor: [
              '#DEB887',
              '#A9A9A9',
              '#DC143C',
              '#F4A460',
              '#2E8B57'
            ],
            borderColor: [
              '#CDA776',
              '#989898',
              '#CB252B',
              '#E39371',
              '#1D7A46'
            ],
            borderWidth: [1, 1, 1, 1, 1]
          }
        ]
      },
      options: {
        responsive: true,
        title: {
          display: true,
          position: 'top',
          text: 'Pie Chart',
          fontSize: 18,
          fontColor: '#111'
        }
      }
    }
  },
  mounted: function () {
    this.getStudent()
    this.renderChart(this.data1, this.options)
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
