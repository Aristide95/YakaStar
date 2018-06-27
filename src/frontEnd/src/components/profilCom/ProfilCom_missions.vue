<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <div v-if="currentStudent.status === 'com'">
        <br />
        <b-nav justified tabs>
          <b-nav-item><router-link :to="{name: 'ProfilCom'}">Profil</router-link></b-nav-item>
          <b-nav-item><router-link :to="{name: 'ProfilComStat'}">Statistiques</router-link></b-nav-item>
          <b-nav-item><router-link :to="{name: 'ProfilComMesMission'}">Mes missions</router-link></b-nav-item>
          <b-nav-item active>Gestion des missions</b-nav-item>
        </b-nav>
        <br />
        <b-container>
          <div class="text-center">
            <b-btn class="btn btn-creation" v-b-modal="'addMissionModal'">Nouvelle mission</b-btn>
          </div>
        </b-container>
        <b-container>
          <h1 class="titre">Missions non publiées</h1>
          <hr class="style-four">
          <b-table striped hover :items="nonPublie" :fields="fields" :current-page="currentPage1" :per-page="perPage">
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
                  <b-col><p v-for="t in row.item.techno" >{{t}}</p></b-col>
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
                    <b>Mission non publiée</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="6" offset="3" style="text-align: center">
                    <b v-if="row.item.state === 0">
                      <b-btn class="btn-info" v-on:click="publish(row.item)">Publier</b-btn>
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
          <b-row>
            <div class="center-block">
              <b-pagination :total-rows="nonPublie.length" :per-page="perPage" v-model="currentPage1" class="my-0" />
            </div>
          </b-row>
        </b-container>
        <b-container>
          <h1 class="titre">Missions publiées</h1>
          <hr class="style-four">
          <b-table striped hover :items="publie" :fields="fields2" :current-page="currentPage3" :per-page="perPage">
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
                    <b>Mission publiée il y {{ row.item.publication_date | moment("from", "now", true) }}</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="6" offset="3" style="text-align: center">
                    <b v-if="row.item.state === 1">
                      <b-btn class="btn-info" v-on:click="getMission(row.item.id)" v-b-modal="'addPresta'">Attribuer un prestataire</b-btn>
                    </b>
                    <b-btn class="btn-danger" v-on:click="abandon(row.item)">Annuler la mission</b-btn>
                  </b-col>
                </b-row>
              </b-card>
            </template>
          </b-table>
          <b-row>
            <div class="center-block">
              <b-pagination :total-rows="publie.length" :per-page="perPage" v-model="currentPage3" class="my-0" />
            </div>
          </b-row>
        </b-container>
        <b-container>
          <h1 class="titre">Missions pourvues</h1>
          <hr class="style-four">
          <b-table striped hover :items="pourvue" :fields="fields2" :current-page="currentPage2" :per-page="perPage">
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
                  <b-col><span v-for="t in row.item.techno" >{{t}} </span></b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="3" class="text-sm-right"><b>Type de mission :</b></b-col>
                  <b-col>{{row.item.type_mission}}</b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="3" class="text-sm-right"><b>Prestataire de la mission :</b></b-col>
                  <b-col>{{ namePresta(row.item.id) }}</b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="4" offset="4" style="text-align: center">
                    <b>Créé il y a {{ row.item.creation_date | moment("from", "now", true) }}</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="4" offset="4" style="text-align: center">
                    <b>Mission pourvue</b>
                  </b-col>
                </b-row>
                <b-row class="mb-2">
                  <b-col sm="6" offset="3" style="text-align: center">
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
          <b-row>
            <div class="center-block">
              <b-pagination :total-rows="pourvue.length" :per-page="perPage" v-model="currentPage2" class="my-0" />
            </div>
          </b-row>
        </b-container>
        <b-container>
          <h1 class="titre">Missions en cours</h1>
          <hr class="style-four">
          <b-table striped hover :items="enCours" :fields="fields2" :current-page="currentPage4" :per-page="perPage">
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
                  <b-col><span v-for="t in row.item.techno" >{{t}} </span></b-col>
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
          <b-row>
            <div class="center-block">
              <b-pagination :total-rows="enCours.length" :per-page="perPage" v-model="currentPage4" class="my-0" />
            </div>
          </b-row>
        </b-container>
        <b-container>
          <h1 class="titre">Missions terminées</h1>
          <hr class="style-four">
          <b-table striped hover :items="termine" :fields="fields2" :current-page="currentPage" :per-page="perPage">
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
                  <b-col><span v-for="t in row.item.techno" >{{t}} </span></b-col>
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
          <b-row>
            <div class="center-block">
              <b-pagination :total-rows="termine.length" :per-page="perPage" v-model="currentPage" class="my-0" />
            </div>
          </b-row>
        </b-container>
        <b-container>
          <h1 class="titre">Missions annulées</h1>
          <hr class="style-four">
          <b-table striped hover :items="annule" :fields="fields2" :current-page="currentPage5" :per-page="perPage">
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
                  <b-col><span v-for="t in row.item.techno" >{{t}} </span></b-col>
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
          <b-row>
            <div class="center-block">
              <b-pagination :total-rows="annule.length" :per-page="perPage" v-model="currentPage5" class="my-0" />
            </div>
          </b-row>
        </b-container>
        <br />

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
              <div v-for="t in technos">
                <input type="checkbox" v-bind:id="t.name" v-bind:value="t.name" v-model="currentMission.technos"/>
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
                  <input type="checkbox" v-bind:id="t.name" v-bind:value="t.name" v-model="checkedNames" />
                  {{t.name}}
                </label>
              </div>
            </b-form-group>
            <b-form-group label="Nouvelle techno : ">
              <b-form-input type="text" v-model="newTech"></b-form-input>
              <b-btn class="btn btn-info" v-on:click="addTechno(newTech)">Ajouter</b-btn>
            </b-form-group>
            <div class="text-center">
              <b-button id="submit" type="submit" variant="primary">Créer</b-button>
            </div>
          </b-form>
        </b-modal>

        <b-modal id="addPresta">
          <h3 class="titre" v-if="postMissionMvp.length > 0">MVP postulant</h3>
          <b-table striped hover :items="postMissionMvp" :fields="fields3" v-if="postMissionMvp.length > 0">
            <template slot="choisir" slot-scope="row">
              <b-btn type="button" class="btn-success" v-on:click="addPresta(row.item.id)"><i class="fas fa-check"></i></b-btn>
            </template>
          </b-table>
          <h3 class="titre">Prestataires postulant</h3>
          <b-table striped hover :items="postMission" :fields="fields3" v-if="postMission.length > 0">
            <template slot="choisir" slot-scope="row">
              <b-btn type="button" class="btn-success" v-on:click="addPresta(row.item.id)"><i class="fas fa-check"></i></b-btn>
            </template>
          </b-table>
          <b-row v-else class="text-center">
            <b>Peronne n'a encore postulé</b>
          </b-row>
          <br />
          <h3 class="titre">Choisir un autre prestataire</h3>
          <b-row>
            <b-col>
              <b-form-group horizontal label="Filtrer :" class="mb-0">
                <b-input-group>
                  <b-form-input v-model="filter1" placeholder="Rechercher un prestataire" />
                  <b-input-group-append>
                    <b-btn :disabled="!filter1" @click="filter1 = ''">Effacer</b-btn>
                  </b-input-group-append>
                </b-input-group>
              </b-form-group>
            </b-col>
          </b-row>
          <br />
          <b-table striped :items="s" :fields="fields3" :filter="filter1" :current-page="currentPage6" :per-page="perPage2">
            <template slot="choisir" slot-scope="row">
              <b-btn type="button" class="btn-success" v-on:click="addPresta(row.item.id)"><i class="fas fa-check"></i></b-btn>
            </template>
          </b-table>
          <b-row>
            <div class="center-block">
              <b-pagination :total-rows="pourvue.length" :per-page="perPage" v-model="currentPage6" class="my-0" />
            </div>
          </b-row>
        </b-modal>
      </div>
      <div v-else>
        <h2 class="titre">Erreur 403 : vous n'avez pas les droits</h2>
        <div style="text-align: center">
          <img class="img-responsive img-fluid" src="../../assets/403.jpg" alt="erreur 403"/>
        </div>
        <h3 class="titre"><router-link :to="{name: 'Accueil'}">Revenir à la page d'accueil</router-link></h3>
      </div>
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
    name: 'ProfilAdmin_missions',
    components: {Footer, Nav},
    data () {
      return {
        missions: [],
        currentPage6: 1,
        perPage2: 3,
        filter1: null,
        selected: [],
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
            key: 'Editer/Supprimer',
            label: 'Editer/Supprimer',
            sortable: false
          }
        ],
        fields2: [
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
        fields3: [
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
            key: 'choisir',
            label: 'Choisir',
            sortable: false
          }
        ],
        loading: false,
        currentMission: {},
        technos: [],
        checkedNames: [],
        publie: [],
        nonPublie: [],
        annule: [],
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
          'techno': []
        },
        currentPage: 1,
        currentPage1: 1,
        currentPage2: 1,
        currentPage3: 1,
        currentPage4: 1,
        currentPage5: 1,
        perPage: 5,
        pageOptions: [ 5, 10, 15 ],
        postMission: [],
        currentStudent: null,
        prestMission: [],
        p: [],
        s: [],
        postMissionMvp: [],
        newTech: null
      }
    },
    mounted: function () {
      this.test()
      this.getMissions()
      this.getTechno()
      this.getStudents()
      this.getPresta_mission()
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
      find (array, index) {
        for (var i = 0; i < array.length; i++) {
          if (array[i].id === index) {
            return array[i].name
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
      addTechno: function (tech) {
        let apirUrl = 'http://127.0.0.1:8000/api/techno/'
        this.loading = true

        var t = {
          'name': tech
        }

        axios.post(apirUrl, t)
          .then((response) => {
            this.missions = response.data
            this.loading = false
            this.getTechno()
            this.newTech = null
          })
          .catch((err) => {
            this.loading = false
            console.log(err)
          })
      },
      getStudents: function () {
        let apirUrl = 'http://127.0.0.1:8000/api/etudiant/'
        this.loading = true
        axios.get(apirUrl)
          .then((response) => {
            this.s = response.data
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
            this.annule.push(missions[i])
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
            this.getPost(this.currentMission.id)
            this.loading = false
          })
          .catch((err) => {
            this.loading = false
            console.log(err)
          })
      },
      getPost: function (id) {
        this.postMission = []
        this.loading = true
        let apiUrl = `http://127.0.0.1:8000/api/postuler/`
        var p = []
        axios.get(apiUrl)
          .then((response) => {
            p = response.data
            for (var i = 0; i < p.length; i++) {
              if (p[i].etudiant_id === this.currentStudent.id && p[i].mission_id === id) {
                var s = {
                  'id': this.currentStudent.id,
                  'firstname': this.currentStudent.firstname,
                  'lastname': this.currentStudent.lastname
                }
                if (this.currentStudent.status === 'mvp') {
                  this.postMissionMvp.push(s)
                } else {
                  this.postMission.push(s)
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
      addPresta: function (id) {
        this.loading = true
        let apirUrl = `http://127.0.0.1:8000/api/presta_mission/`
        var p = {
          'mission_id': this.currentMission.id,
          'etudiant_id': id
        }
        axios.post(apirUrl, p)
          .then((response) => {
            this.loading = false
            location.reload()
          })
          .catch((err) => {
            this.loading = false
            console.log(err)
          })

        this.loading = true
        let apirUrl2 = `http://127.0.0.1:8000/api/mission/${this.currentMission.id}/`
        this.currentMission.state = 2
        axios.put(apirUrl2, this.currentMission)
          .then((response) => {
            this.loading = false
            this.currentMission = response.data
            this.getMissions()
            location.reload()
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
            location.reload()
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

        var t = []
        for (var i = 0; i < mission.techno.length; i++) {
          for (var j = 0; j < this.technos.length; j++) {
            if (mission.techno[i] === this.technos[j].name) {
              t.push(this.technos[j].id)
            }
          }
        }

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
          'techno': t
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

        var tech = []

        for (var i = 0; i < this.technos.length; i++) {
          for (var j = 0; j < this.checkedNames.length; j++) {
            if (this.technos[i].name === this.checkedNames[j]) {
              tech.push(this.technos[i].id)
            }
          }
        }

        this.newMission.techno = tech

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
      },
      namePresta: function (id) {
        for (var i = 0; i < this.p.length; i++) {
          if (this.p[i].mission_id === id) {
            for (var j = 0; j < this.s.length; j++) {
              if (this.s[j].id === this.p[i].etudiant_id) {
                var name = this.s[j].firstname + ' ' + this.s[j].lastname
                return name
              }
            }
          }
        }
        return null
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
  .center-block {
    margin-left:auto;
    margin-right:auto;
    display:block;
  }
  .btn-creation {
    background-color: #79b249;
    border-color: #598236;
  }
</style>
