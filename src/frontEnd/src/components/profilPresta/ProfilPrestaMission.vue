<template>
    <div class="profilPrestaMissions">
      <Nav></Nav>
      <b-container>
        <br />
        <b-nav justified tabs>
          <b-nav-item><router-link :to="{name: 'ProfilPresta'}">Profil</router-link></b-nav-item>
          <b-nav-item active>Mes missions</b-nav-item>
        </b-nav>
        <b-container>
          <h1 class="titre">Mes missions</h1>
          <hr class="style-four">
          <b-table striped hover :items="publie" :fields="fields"></b-table>
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
    name: 'ProfilPrestaMission',
    components: {Footer, Nav},
    data () {
      return {
        missions: [],
        publie: [],
        fields: [ 'title', 'type_mission', 'state' ],
        loading: false
      }
    },
    mounted: function () {
      this.getMissions()
    },
    methods: {
      getMissions: function () {
        let apirUrl = 'http://127.0.0.1:8000/api/mission/'
        this.loading = true
        axios.get(apirUrl)
          .then((response) => {
            this.missions = response.data
            this.sortMission(this.missions)
            for (var i = 0; i < this.missions.length; i++) {
              var tab = (this.missions[i].techno)
              var test = []
              for (var j = 0; j < tab.length; j++) {
                for (var k = 0; k < this.technos.length; k++) {
                  if (tab[j] === this.technos[k].id) {
                    test.push(this.technos[k].name)
                  }
                }
              }
              this.missions[i].techno = test
            }
            this.loading = false
          })
          .catch((err) => {
            this.loading = false
            console.log(err)
          })
      },
      sortMission: function (missions) {
        for (var i = 0; i < missions.length; i++) {
          if (missions[i].state === 0) {
            this.nonPublie.push(missions[i])
          } else if (missions[i].state === 1) {
            this.publie.push(missions[i])
          } else if (missions[i].state === 2) {
            this.pourvue.push(missions[i])
          } else if (missions[i].state === 3) {
            this.enCours.push(missions[i])
          } else if (missions[i].state === 4) {
            this.termine.push(missions[i])
          } else {
            this.annulé.push(missions[i])
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
