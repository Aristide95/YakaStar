<template>
    <div class="profilPrestaMissions">
      <Nav></Nav>
      <b-container>
        <div v-if="currentStudent === [] || currentStudent.status === 'com' || currentStudent.status === 'admin'">
          <h2 class="titre">Erreur 403 : vous n'avez pas les droits</h2>
          <div style="text-align: center">
            <img class="img-responsive img-fluid" src="../../assets/403.jpg" alt="erreur 403"/>
          </div>
          <h3 class="titre"><router-link :to="{name: 'Accueil'}">Revenir à la page d'accueil</router-link></h3>
        </div>
        <div v-else>
          <br />
          <b-nav justified tabs>
            <b-nav-item><router-link :to="{name: 'ProfilPresta'}">Profil</router-link></b-nav-item>
            <b-nav-item active>Mes missions</b-nav-item>
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
                  <b-row class="mb-2">
                    <b-col sm="4" offset="4" style="text-align: center">
                      <b-btn class="btn btn-info" v-if="row.item.state === 2" v-on:click="showDevis (row.item)">Voir le devis</b-btn>
                    </b-col>
                  </b-row>
                </b-card>
              </template>
              <template slot="status" slot-scope="row">
                <b-btn class="btn btn-info" v-if="row.item.state === 2" v-on:click="start(row.item)">Accepter le devis</b-btn>
                <b-btn class="btn btn-danger" v-if="row.item.state === 3" v-on:click="finished(row.item)">Terminer la mission</b-btn>
                <b v-if="row.item.state === 4">Mission terminée</b>
              </template>
            </b-table>
          </b-container>
          <div style="padding-bottom: 7%"></div>
        </div>
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
      technos: [],
      presta_mission: [],
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
        },
        {
          key: 'status',
          label: 'Status',
          sortable: false
        }
      ],
      loading: false,
      mes_missions: [],
      mes_missions_id: [],
      currentStudent: [],
      data: [],
      tmp: []
    }
  },
  mounted: function () {
    this.test()
    this.getMissions()
    this.getPresta_mission()
    this.getTechno()
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
          for (var k = 0; k < this.presta_mission.length; k++) {
            if (this.presta_mission[k].etudiant_id === this.currentStudent.id) {
              this.mes_missions_id.push(this.presta_mission[k])
            }
          }
          for (var i = 0; i < this.mes_missions_id.length; i++) {
            for (var j = 0; j < this.missions.length; j++) {
              if (this.mes_missions_id[i].mission_id === this.missions[j].id) {
                this.mes_missions.push(this.missions[j])
              }
            }
          }
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
          this.presta_mission = response.data
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    getTechno: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/techno/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.technos = response.data
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    getMissions: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/mission/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.missions = response.data
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
    start: function (mission) {
      this.loading = true
      let apiUrl = `http://127.0.0.1:8000/api/mission/${mission.id}/`

      axios.get(apiUrl)
        .then((response) => {
          this.tmp = response.data
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })

      var tech = []

      for (var i = 0; i < this.technos.length; i++) {
        for (var j = 0; j < mission.techno.length; j++) {
          if (this.technos[i].name === mission.techno[j]) {
            tech.push(this.technos[j].id)
          }
        }
      }

      console.log(tech)

      var update = {
        'title': mission.title,
        'desc': mission.desc,
        'type_mission': mission.type_mission,
        'state': 3,
        'creation_date': mission.creation_date,
        'publication_date': mission.publication_date,
        'client_name': mission.client_name,
        'logo_url': mission.logo_url,
        'devis_url': mission.devis_url,
        'num_presta': mission.num_presta,
        'commercial_id': mission.commercial_id,
        'techno': tech
      }

      console.log(update)
      axios.put(apiUrl, update)
        .then((response) => {
          this.loading = false
          location.reload()
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    finished: function (mission) {
      this.loading = true
      let apiUrl = `http://127.0.0.1:8000/api/mission/${mission.id}/`

      axios.get(apiUrl)
        .then((response) => {
          this.tmp = response.data
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })

      var tech = []

      for (var i = 0; i < this.technos.length; i++) {
        for (var j = 0; j < mission.techno.length; j++) {
          if (this.technos[i].name === mission.techno[j]) {
            tech.push(this.technos[j].id)
          }
        }
      }

      console.log(tech)

      var update = {
        'title': mission.title,
        'desc': mission.desc,
        'type_mission': mission.type_mission,
        'state': 4,
        'creation_date': mission.creation_date,
        'publication_date': mission.publication_date,
        'client_name': mission.client_name,
        'logo_url': mission.logo_url,
        'devis_url': mission.devis_url,
        'num_presta': mission.num_presta,
        'commercial_id': mission.commercial_id,
        'techno': tech
      }

      axios.put(apiUrl, update)
        .then((response) => {
          this.loading = false
          location.reload()
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
</style>
