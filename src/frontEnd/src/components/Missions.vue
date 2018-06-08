<template>
    <div id="missions">
      <Nav></Nav>
      <b-container>
        <h1 class="titre">Nos missions</h1>
        <hr class="style-four">
        <div class="mfiltre">
          <b-row>
            <b-col sm="6" offset="3">
              <b-form-group horizontal label="Filtrer :" class="mb-0">
                <b-input-group>
                  <b-form-input v-model="filter" placeholder="Rechercher une mission" />
                  <b-input-group-append>
                    <b-btn :disabled="!filter" @click="filter = ''">Effacer</b-btn>
                  </b-input-group-append>
                </b-input-group>
              </b-form-group>
            </b-col>
          </b-row>
        </div>
        <br />
      </b-container>
      <b-container class="m">
        <b-table striped hover :items="publie" :fields="fields" :filter="filter" :current-page="currentPage" :per-page="perPage">
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
                  <b>Mission publiée il y {{ row.item.publication_date | moment("from", "now", true) }}</b>
                </b-col>
              </b-row>
            </b-card>
          </template>
          <template slot="sinscrire" slot-scope="row">
            <b-btn class="btn btn-info" v-if="check(row.item.id)" v-on:click="postuler(row.item.id)">Postuler</b-btn>
            <b v-else>Déja postulé</b>
          </template>
        </b-table>
        <b-row>
          <div class="center-block">
            <b-pagination :total-rows="publie.length" :per-page="perPage" v-model="currentPage" class="my-0" />
          </div>
        </b-row>
      </b-container>
      <Footer></Footer>
    </div>
</template>

<script>
import Nav from './Nav'
import Footer from './Footer'
import axios from 'axios'
export default {
  name: 'Missions',
  components: {Footer, Nav},
  data () {
    return {
      missions: [],
      technos: [],
      oneTechno: null,
      checkedNames: [],
      currentMission: {},
      loading: false,
      filter: null,
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
        },
        {
          key: 'sinscrire',
          label: 'Postuler',
          sortable: false
        }
      ],
      currentPage: 1,
      perPage: 10,
      pageOptions: [10, 20, 30],
      student: [],
      post: []
    }
  },
  mounted: function () {
    this.getMissions()
    this.test()
    this.getPost()
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
          this.getStudent(response.data['user_id'])
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
    getStudent: function (userId) {
      let apirUrl = 'http://127.0.0.1:8000/api/etudiant/' + userId
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
    sortMission: function (missions) {
      for (var i = 0; i < missions.length; i++) {
        if (missions[i].state === 1) {
          this.publie.push(missions[i])
        }
      }
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
          this.sortMission(this.missions)
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
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
    postuler: function (missionId) {
      let apirUrl = 'http://127.0.0.1:8000/api/postuler/'
      this.loading = true
      var newPostule = {
        'etudiant_id': this.student.id,
        'mission_id': missionId
      }
      axios.post(apirUrl, newPostule)
        .then((response) => {
          this.missions = response.data
          this.loading = false
          location.reload()
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    getPost: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/postuler/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.post = response.data
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    check: function (missionId) {
      for (var i = 0; i < this.post.length; i++) {
        if (this.post[i].mission_id === missionId && this.post[i].etudiant_id === this.student.id) {
          return false
        }
      }
      return true
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
    padding-top: 5px;
    padding-bottom: 5px;
  }
  .center-block {
    margin-left:auto;
    margin-right:auto;
    display:block;
  }
  .mfiltre {
    padding-top: 5%;
    padding-bottom: 2%;
  }
  .m {
    padding-bottom: 5%;
  }
</style>
