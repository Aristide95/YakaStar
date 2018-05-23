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
        <b-container>
          <h1 class="titre">Mes missions</h1>
          <hr class="style-four">
          <b-table striped hover :items="publie" :fields="fields">
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
      </b-nav>
    </b-container>

    <Footer></Footer>
  </div>
</template>

<script>
import Nav from '../Nav'
import Footer from '../Footer'
import axios from 'axios'
import moment from 'moment'
export default {
  name: 'ProfilAdmin_mesMission',
  components: {Footer, Nav},
  data () {
    return {
      missions: [],
      publie: [],
      fields: [
        {
          key: 'title',
          label: 'titre',
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
      currentMission: {},
      oneTechno: null,
      checkedNames: [],
      newMission: {
        'title': null,
        'desc': null,
        'type_mission': null,
        'state': 0,
        'creation_date': new Date(),
        'publication_date': null,
        'client_name': null,
        'logo_url': null,
        'devis_url': null,
        'num_presta': 1,
        'commercial_id': 1,
        'techno': [1]
      }
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
    },
    deleteMission: function (id) {
      let apirUrl = `http://127.0.0.1:8000/api/mission/${id}/`
      this.loading = true
      axios.delete(apirUrl)
        .then((response) => {
          this.loading = false
          this.getMissions()
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    getMission: function (id) {
      this.loading = true
      let apiUrl = `http://127.0.0.1:8000/api/mission/${id}/`
      axios.get(apiUrl)
        .then((response) => {
          this.currentMission = response.data
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    updateMission: function () {
      this.loading = true
      let apirUrl = `http://127.0.0.1:8000/api/mission/${this.currentMission.id}/`
      axios.put(apirUrl, this.currentMission)
        .then((response) => {
          this.loading = false
          this.currentMission = response.data
          this.getMissions()
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    publish: function (mission) {
      this.loading = true
      let now = moment().format()
      moment.locale('fr')
      var update = {
        'title': mission.title,
        'desc': mission.desc,
        'type_mission': mission.type_mission,
        'state': 1,
        'creation_date': mission.creation_date,
        'publication_date': now,
        'client_name': mission.client_name,
        'logo_url': mission.logo_url,
        'devis_url': mission.devis_url,
        'num_presta': mission.num_presta,
        'commercial_id': mission.commercial_id,
        'techno': [1]
      }
      let apirUrl = `http://127.0.0.1:8000/api/mission/${mission.id}/`
      axios.put(apirUrl, update)
        .then((response) => {
          this.loading = false
          this.currentMission = response.data
          location.reload()
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    abandon: function (mission) {
      this.loading = true
      var update = {
        'title': mission.title,
        'desc': mission.desc,
        'type_mission': mission.type_mission,
        'state': 5,
        'creation_date': mission.creation_date,
        'client_name': mission.client_name,
        'logo_url': mission.logo_url,
        'devis_url': mission.devis_url,
        'num_presta': mission.num_presta,
        'commercial_id': mission.commercial_id,
        'techno': [1]
      }
      let apirUrl = `http://127.0.0.1:8000/api/mission/${mission.id}/`
      axios.put(apirUrl, update)
        .then((response) => {
          this.loading = false
          this.currentMission = response.data
          location.reload()
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    addMission: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/mission/'
      this.loading = true
      axios.post(apirUrl, this.newMission)
        .then((response) => {
          this.missions = response.data
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
