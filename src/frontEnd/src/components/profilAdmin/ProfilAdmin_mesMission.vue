<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <br />
      <b-nav justified tabs>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_profil'}">Profil</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_statistique'}">Statistiques</router-link></b-nav-item>
        <b-nav-item active>Mes missions</b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_missions'}">Gestion des missions</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_utilisateurs'}">Gestion des utilisateurs</router-link></b-nav-item>
      </b-nav>
      <b-container>
        <h1 class="titre">Mes missions</h1>
        <hr class="style-four">
        <b-table striped hover :items="mes_missions" :fields="fields">
          <template slot="show_details" slot-scope="row">
            <b-button size="sm" @click.stop="row.toggleDetails" class="mr-2">
              Voir {{ row.detailsShowing ? 'moins' : 'plus'}}
            </b-button>
          </template>
          <template slot="row-details" slot-scope="row">
            <b-card>
              <b-row class="mb-2">
                <b-col sm="3" class="text-sm-right"><b>Description :</b></b-col>
                <b-col>{{row.item.desc}}</b-col>
              </b-row>
              <b-row class="mb-2">
                <b-col sm="3" class="text-sm-right"><b>Technos :</b></b-col>
                <b-col><p v-for="t in row.item.techno" >{{t}} </p></b-col>
              </b-row>
              <b-row class="mb-2">
                <b-col sm="3" class="text-sm-right"><b>Type de mission :</b></b-col>
                <b-col>{{row.item.type_mission}}</b-col>
              </b-row>
              <b-row class="mb-2">
                <b-col sm="4" offset="4" style="text-align: center">
                  <b v-if="row.item.state === 1">Mission publiée il y a {{ row.item.publication_date | moment("from", "now", true) }}</b>
                </b-col>
              </b-row>
            </b-card>
          </template>
        </b-table>
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
  name: 'ProfilAdmin_mesMission',
  components: {Footer, Nav},
  data () {
    return {
      missions: [],
      getPresta_mission: [],
      publie: [],
      fields: [
        {
          key: 'title',
          label: 'Titre',
          sortable: true
        },
        {
          key: 'client_name',
          label: 'Client',
          sortable: true
        },
        {
          key: 'show_details',
          label: 'Voir plus',
          sortable: false
        }
      ],
      loading: false,
      mes_missions: [],
      currentStudent: [],
      p: []
    }
  },
  mounted: function () {
    this.getPresta_mission()
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
          this.p = response.data
          this.mesMissions()
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    mesMissions: function () {
      var id = this.currentStudent.id
      for (var i = 0; i < this.p.length; i++) {
        if (this.p[i].etudiant_id === id) {
          this.mes_missions.push(this.p[i])
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
        if (missions[i].state === 1) {
          this.publie.push(missions[i])
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
