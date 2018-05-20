<template>
    <div id="missions">
      <Nav></Nav>
      <b-container>
        <h1 class="titre">Nos missions</h1>
        <hr class="style-four">
        <h2 class="titre"> Filtrer la recherche</h2>
        <b-row>
          <b-col sm="8">
            <div v-for="t in technos">
              <input type="checkbox" v-bind:id="t.name" v-bind:value="t.name" v-model="checkedNames"/>
              <label v-bind:for="t.name">{{t.name}}</label>
            </div>
          </b-col>
          <b-col sm="4">
            <form class="navbar-form" role="search">
              <div class="input-group add-on">
                <input class="form-control" placeholder="Recherche" name="srch-term" id="srch-term" type="text">
                <div class="input-group-btn">
                  <button class="btn btn-default" type="submit"><i class="fas fa-search"></i></button>
                </div>
              </div>
            </form>
          </b-col>
        </b-row>
      </b-container>
      <b-container>
        <div v-for="m in missions">
          <b-row class="mission">
            <b-col sm="4">
              <b-btn class="btn-danger" v-on:click="deleteMission(m.id)"><i class="fas fa-times"></i></b-btn>
              <b-btn type="button" class="btn-success" v-on:click="getMission(m.id)" v-b-modal="'editMissionModal'"><i class="fas fa-edit"></i></b-btn>
            </b-col>
            <b-col sm="4">
              <h5 v-bind:for="m.title" class="titre">{{ m.title }}</h5>
            </b-col>
            <b-col sm="4">
              <p style="text-align: right; padding-top: 5px">créé il y a {{ m.creation_date | moment("from", "now", true) }}</p>
            </b-col>
            <b-container>
              <b-row>
                <b-col sm="4">
                  <p>Type de la mission : <strong>{{m.type_mission}}</strong></p>
                </b-col>
                <b-col sm="4" offset="4">
                  <p style="text-align: right">Etat : <strong v-if="m.state == 0">non-publié</strong><strong v-else>publié</strong></p>
                </b-col>
              </b-row>
              <b-row>
                <p style="text-align: justify">{{m.desc}}</p>
              </b-row>
              <b-row>
                <b-col sm="3"><span>Technos :
                    <ul v-for="t in m.techno">
                      <li class="list-inline-item"> <strong>{{t}}</strong></li>
                    </ul>
                  </span>
                </b-col>
                <b-col sm="3" offset="6" class="text-center">
                  <b-btn class="btn-info" v-if="m.state == 0">publier</b-btn>
                  <p v-else>publié il y a {{ m.publication_date | moment("from", "now", true) }}</p>
                </b-col>
              </b-row>
            </b-container>
          </b-row>
        </div><br />
      </b-container>
      <b-container>
        <div class="text-center">
          <b-btn class="btn-creation" href="#/creation-mission">Nouvelle mission</b-btn>
        </div>
      </b-container>
      <Footer></Footer>

      <b-modal id="editMissionModal">
        <form v-on:submit.prevent="updateMission()">
          <b-form-group label="Titre de la mission">
            <b-form-input type="text" v-model="currentMission.title" required placeholder="Obligatoire"></b-form-input>
          </b-form-group>
          <b-form-group label="Type de la mission">
            <select v-model="currentMission.type_mission">
              <option>Applicatif</option>
              <option>Audit</option>
              <option>Conception</option>
              <option>Formation</option>
              <option>Gestion</option>
              <option>Maintenance</option>
              <option>Sécurité</option>
              <option>Web</option>
            </select>
          </b-form-group>
          <b-form-group label="Nom du client">
            <b-form-input type="text" v-model="currentMission.client_name" required placeholder="Obligatoire"></b-form-input>
          </b-form-group>
          <b-form-group label="Nombre de prestataires sur la mission">
            <b-form-input type="number" v-model="currentMission.num_presta" required placeholder="Obligatoire"></b-form-input>
          </b-form-group>
          <b-form-group label="Description">
            <b-form-textarea v-model="currentMission.desc" placeholder="Obligatoire"
                             :rows="3"
                             :max-rows="6"
                             required >
            </b-form-textarea>
          </b-form-group>
          <b-form-group label="Technologies de la mission">
            <div v-for="t in techno">
              <input type="checkbox" v-bind:id="t.name" v-bind:value="t.name" v-model="checkedNames"/>
              <label v-bind:for="t.name">{{t.name}}</label>
            </div>
          </b-form-group>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary m-progress" data-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-primary">Save changes</button>
          </div>
        </form>
      </b-modal>
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
      missions: this.getMission(),
      technos: this.getTechno(),
      oneTechno: null,
      checkedNames: [],
      currentMission: {},
      loading: false
    }
  },
  mounted: function () {
    this.getMissions()
  },
  methods: {
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
    getOneTechno: function (id) {
      let apirUrl = `http://127.0.0.1:8000/api/techno/${id}/`
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.oneTechno = response.data
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
    }
  }
}
</script>

<style scoped>
  .mission {
    background-color: #F5F7F9;
    border: 1px solid #ddd;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
    border-radius: 5px;
    margin-top: 10px;
    padding: 1%;
  }
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
  .btn-creation {
    background-color: #79b249;
    border-color: #598236;
  }
</style>
