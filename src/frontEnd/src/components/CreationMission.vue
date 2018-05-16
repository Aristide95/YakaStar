<template>
  <div id="creation">
    <Nav></Nav>
    <b-container>
      <h1 class="titre">Création d'une mission</h1>
      <hr class="style-four">
      <b-col sm="6" offset="3" id="formulaire">
        <b-form v-on:submit.prevent="addMission()" v-if="show">
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
            <div v-for="t in techno">
              <input type="checkbox" v-bind:id="t.name" v-bind:value="t.name" v-model="checkedNames"/>
              <label v-bind:for="t.name">{{t.name}}</label>
            </div>
          </b-form-group>
          <div class="text-center">
            <b-button id="submit" type="submit" variant="primary">Créer</b-button>
          </div>
        </b-form>
      </b-col>
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Nav from './Nav'
import Footer from './Footer'
import axios from 'axios'
export default {
  name: 'CreationMission',
  components: {Footer, Nav},
  data () {
    return {
      techno: this.getTechno(),
      checkedNames: [],
      show: true,
      file: null,
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
    this.getTechno()
  },
  methods: {
    getTechno: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/techno/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.techno = response.data
          this.loading = false
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
          this.mission = response.data
          this.loading = false
          document.location.href = '#/missions/'
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
