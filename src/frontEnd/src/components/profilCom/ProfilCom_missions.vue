<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <br />
      <b-nav justified tabs>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_profil'}">Profil</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_statistique'}">Statistiques</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_mesMission'}">Mes mission</router-link></b-nav-item>
        <b-nav-item active>Gestion des missions</b-nav-item>
      </b-nav>
        <b-container>
          <h1 class="titre">Missions non publiées</h1>
          <hr class="style-four">
          <b-table striped hover :items="nonPublie" :fields="fields">
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
                    <b>Créé il y a {{ row.item.creation_date | moment("from", "now", true) }}</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="4" offset="4" style="text-align: center">
                    <b v-if="row.item.state === 0">Mission non publiée</b>
                    <b v-if="row.item.state === 1">Mission publiée</b>
                    <b v-if="row.item.state === 2">Mission pourvue</b>
                    <b v-if="row.item.state === 3">Mission en cours</b>
                    <b v-if="row.item.state === 4">Mission terminée</b>
                    <b v-if="row.item.state === 5">Mission annulée</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="6" offset="3" style="text-align: center">
                    <b v-if="row.item.state === 0">
                      <b-btn class="btn-info" v-on:click="publish(row.item)">Publier</b-btn>
                    </b>
                    <b v-if="row.item.state === 1">
                      <b-btn class="btn-info">Attribuer un prestataire</b-btn>
                    </b>
                    <b-btn class="btn-danger" v-on:click="abandon(row.item)">Annuler la mission</b-btn>
                  </b-col>
                </b-row>
              </b-card>
            </template>
            <template slot="Editer/Supprimer" slot-scope="row">
              <b-btn class="btn-danger" v-on:click="deleteMission(row.item.id)"><i class="fas fa-times"></i></b-btn>
              <b-btn type="button" class="btn-success" v-on:click="getMission(row.item.id)" v-b-modal="'editMissionModal'"><i class="fas fa-edit"></i></b-btn>
            </template>
          </b-table>
        </b-container>
        <b-container>
          <h1 class="titre">Missions publiées</h1>
          <hr class="style-four">
          <b-table striped hover :items="publie" :fields="fields2">
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
                    <b>Créé il y a {{ row.item.creation_date | moment("from", "now", true) }}</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="4" offset="4" style="text-align: center">
                    <b v-if="row.item.state === 0">Mission non publiée</b>
                    <b v-if="row.item.state === 1">Mission publiée il y {{ row.item.publication_date | moment("from", "now", true) }}</b>
                    <b v-if="row.item.state === 2">Mission pourvue</b>
                    <b v-if="row.item.state === 3">Mission en cours</b>
                    <b v-if="row.item.state === 4">Mission terminée</b>
                    <b v-if="row.item.state === 5">Mission annulée</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="6" offset="3" style="text-align: center">
                    <b v-if="row.item.state === 0">
                      <b-btn class="btn-info" v-on:click="publish(row.item)">Publier</b-btn>
                    </b>
                    <b v-if="row.item.state === 1">
                      <b-btn class="btn-info">Attribuer un prestataire</b-btn>
                    </b>
                    <b-btn class="btn-danger" v-on:click="abandon(row.item)">Annuler la mission</b-btn>
                  </b-col>
                </b-row>
              </b-card>
            </template>
            <template slot="Editer/Supprimer" slot-scope="row">
              <b-btn class="btn-danger" v-on:click="deleteMission(row.item.id)"><i class="fas fa-times"></i></b-btn>
              <b-btn type="button" class="btn-success" v-on:click="getMission(row.item.id)" v-b-modal="'editMissionModal'"><i class="fas fa-edit"></i></b-btn>
            </template>
          </b-table>
        </b-container>
        <b-container>
          <h1 class="titre">Missions pourvues</h1>
          <hr class="style-four">
          <b-table striped hover :items="pourvue" :fields="fields2">
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
                    <b>Créé il y a {{ row.item.creation_date | moment("from", "now", true) }}</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="4" offset="4" style="text-align: center">
                    <b v-if="row.item.state === 0">Mission non publiée</b>
                    <b v-if="row.item.state === 1">Mission publiée</b>
                    <b v-if="row.item.state === 2">Mission pourvue</b>
                    <b v-if="row.item.state === 3">Mission en cours</b>
                    <b v-if="row.item.state === 4">Mission terminée</b>
                    <b v-if="row.item.state === 5">Mission annulée</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="6" offset="3" style="text-align: center">
                    <b v-if="row.item.state === 0">
                      <b-btn class="btn-info" v-on:click="publish(row.item)">Publier</b-btn>
                    </b>
                    <b v-if="row.item.state === 1">
                      <b-btn class="btn-info">Attribuer un prestataire</b-btn>
                    </b>
                    <b-btn class="btn-danger" v-on:click="abandon(row.item)">Annuler la mission</b-btn>
                  </b-col>
                </b-row>
              </b-card>
            </template>
            <template slot="Editer/Supprimer" slot-scope="row">
              <b-btn class="btn-danger" v-on:click="deleteMission(row.item.id)"><i class="fas fa-times"></i></b-btn>
              <b-btn type="button" class="btn-success" v-on:click="getMission(row.item.id)" v-b-modal="'editMissionModal'"><i class="fas fa-edit"></i></b-btn>
            </template>
          </b-table>
        </b-container>
        <b-container>
          <h1 class="titre">Missions en cours</h1>
          <hr class="style-four">
          <b-table striped hover :items="enCours" :fields="fields2">
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
                    <b>Créé il y a {{ row.item.creation_date | moment("from", "now", true) }}</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="4" offset="4" style="text-align: center">
                    <b v-if="row.item.state === 0">Mission non publiée</b>
                    <b v-if="row.item.state === 1">Mission publiée</b>
                    <b v-if="row.item.state === 2">Mission pourvue</b>
                    <b v-if="row.item.state === 3">Mission en cours</b>
                    <b v-if="row.item.state === 4">Mission terminée</b>
                    <b v-if="row.item.state === 5">Mission annulée</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="6" offset="3" style="text-align: center">
                    <b v-if="row.item.state === 0">
                      <b-btn class="btn-info" v-on:click="publish(row.item)">Publier</b-btn>
                    </b>
                    <b v-if="row.item.state === 1">
                      <b-btn class="btn-info">Attribuer un prestataire</b-btn>
                    </b>
                    <b-btn class="btn-danger" v-on:click="abandon(row.item)">Annuler la mission</b-btn>
                  </b-col>
                </b-row>
              </b-card>
            </template>
            <template slot="Editer/Supprimer" slot-scope="row">
              <b-btn class="btn-danger" v-on:click="deleteMission(row.item.id)"><i class="fas fa-times"></i></b-btn>
              <b-btn type="button" class="btn-success" v-on:click="getMission(row.item.id)" v-b-modal="'editMissionModal'"><i class="fas fa-edit"></i></b-btn>
            </template>
          </b-table>
        </b-container>
        <b-container>
          <h1 class="titre">Missions terminées</h1>
          <hr class="style-four">
          <b-table striped hover :items="termine" :fields="fields2">
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
                    <b>Créé il y a {{ row.item.creation_date | moment("from", "now", true) }}</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="4" offset="4" style="text-align: center">
                    <b v-if="row.item.state === 0">Mission non publiée</b>
                    <b v-if="row.item.state === 1">Mission publiée</b>
                    <b v-if="row.item.state === 2">Mission pourvue</b>
                    <b v-if="row.item.state === 3">Mission en cours</b>
                    <b v-if="row.item.state === 4">Mission terminée</b>
                    <b v-if="row.item.state === 5">Mission annulée</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="6" offset="3" style="text-align: center">
                    <b v-if="row.item.state === 0">
                      <b-btn class="btn-info" v-on:click="publish(row.item)">Publier</b-btn>
                    </b>
                    <b v-if="row.item.state === 1">
                      <b-btn class="btn-info">Attribuer un prestataire</b-btn>
                    </b>
                    <b-btn class="btn-danger" v-on:click="abandon(row.item)">Annuler la mission</b-btn>
                  </b-col>
                </b-row>
              </b-card>
            </template>
            <template slot="Editer/Supprimer" slot-scope="row">
              <b-btn class="btn-danger" v-on:click="deleteMission(row.item.id)"><i class="fas fa-times"></i></b-btn>
              <b-btn type="button" class="btn-success" v-on:click="getMission(row.item.id)" v-b-modal="'editMissionModal'"><i class="fas fa-edit"></i></b-btn>
            </template>
          </b-table>
        </b-container>
        <b-container>
          <h1 class="titre">Missions annulées</h1>
          <hr class="style-four">
          <b-table striped hover :items="annulé" :fields="fields2">
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
                    <b>Créé il y a {{ row.item.creation_date | moment("from", "now", true) }}</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="4" offset="4" style="text-align: center">
                    <b>Mission annulée</b>
                  </b-col>
                </b-row>
              </b-card>
            </template>
          </b-table>
        </b-container>

        <b-container>
          <div class="text-center">
            <b-btn class="btn-creation" v-b-modal="'addMissionModal'">Nouvelle mission</b-btn>
          </div>
        </b-container>

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

        <b-modal id="addMissionModal">
          <b-form v-on:submit.prevent="addMission()">
            <b-form-group label="Titre de la mission">
              <b-form-input type="text" v-model="newMission.title" required placeholder="Obligatoire"></b-form-input>
            </b-form-group>
            <b-form-group label="Type de la mission">
              <select v-model="newMission.type_mission">
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
              <b-form-input type="text" v-model="newMission.client_name" required placeholder="Obligatoire"></b-form-input>
            </b-form-group>
            <b-form-group label="Nombre de prestataires sur la mission">
              <b-form-input type="number" v-model="newMission.num_presta" required placeholder="Obligatoire"></b-form-input>
            </b-form-group>
            <b-form-group label="Description">
              <b-form-textarea v-model="newMission.desc" placeholder="Obligatoire"
                               :rows="3"
                               :max-rows="6"
                               required >
              </b-form-textarea>
            </b-form-group>
            <b-form-group label="Technologies de la mission">
              <div v-for="t in technos">
                <label class="checkbox-inline" v-bind:for="t.name">
                  <input type="checkbox" v-bind:id="t.name" v-bind:value="t.name" v-model="checkedNames"/>
                  {{t.name}}
                </label>
              </div>
            </b-form-group>
            <div class="text-center">
              <b-button id="submit" type="submit" variant="primary">Créer</b-button>
            </div>
          </b-form>
        </b-modal>
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Nav from '../Nav'
import Footer from '../Footer'
import axios from 'axios'
import * as moment from 'moment'
export default {
  name: 'ProfilCom_missions',
  components: {Footer, Nav},
  data () {
    return {
      missions: [],
      fields: ['title', 'client_name', 'show_details', 'Editer/Supprimer'],
      fields2: ['title', 'client_name', 'show_details'],
      technos: this.getTechno(),
      oneTechno: null,
      checkedNames: [],
      currentMission: {},
      loading: false,
      publie: [],
      nonPublie: [],
      annulé: [],
      pourvue: [],
      enCours: [],
      termine: [],
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
