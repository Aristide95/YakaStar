<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <div v-if="currentStudent.status === 'admin'">
        <br />
        <b-nav justified tabs>
          <b-nav-item><router-link :to="{name: 'ProfilAdmin_profil'}">Profil</router-link></b-nav-item>
          <b-nav-item><router-link :to="{name: 'ProfilAdmin_statistique'}">Statistiques</router-link></b-nav-item>
          <b-nav-item><router-link :to="{name: 'ProfilAdmin_mesMission'}">Mes missions</router-link></b-nav-item>
          <b-nav-item><router-link :to="{name: 'ProfilAdmin_missions'}">Gestion des missions</router-link></b-nav-item>
          <b-nav-item active>Gestion des utilisateurs</b-nav-item>
        </b-nav>

        <b-container>
          <h1 class="titre">Utilisateurs</h1>
          <hr class="style-four">
          <b-container>
            <b-row>
              <b-col sm="4" class="center-block">
                <b-btn class="btn-info" v-on:click="createPDF()">Exporter la liste des membres de CRISTAL</b-btn>
              </b-col>
            </b-row>
            <h2 class="titre">Membre de CRISTAL</h2>
            <hr class="style-four">
            <b-row>
              <b-col sm="6" offset="3">
                <b-form-group horizontal label="Filtrer :" class="mb-0">
                  <b-input-group>
                    <b-form-input v-model="filter1" placeholder="Rechercher un membre CRISTAL" />
                    <b-input-group-append>
                      <b-btn :disabled="!filter1" @click="filter1 = ''">Effacer</b-btn>
                    </b-input-group-append>
                  </b-input-group>
                </b-form-group>
              </b-col>
            </b-row>
            <br />
            <b-table striped :items="admin" :fields="fields2" :filter="filter1" :current-page="currentPage" :per-page="perPage">
              <template slot="modifierDroits" slot-scope="row">
                <b-btn type="button" class="btn-info" v-on:click="getStudent(row.item.id)" v-b-modal="'changeState'"><i class="fas fa-edit"></i></b-btn>
              </template>
              <template slot="Modifier" slot-scope="row">
              </template>
            </b-table>
            <b-row v-if="admin.length > 0">
              <div class="center-block">
                <b-pagination :total-rows="admin.length" :per-page="perPage" v-model="currentPage" class="my-0" />
              </div>
            </b-row>
          </b-container>
          <b-container>
            <h2 class="titre">Commercial de CRISTAL</h2>
            <hr class="style-four">
            <b-row>
              <b-col sm="6" offset="3">
                <b-form-group horizontal label="Filtrer :" class="mb-0">
                  <b-input-group>
                    <b-form-input v-model="filter" placeholder="Rechercher un commercial" />
                    <b-input-group-append>
                      <b-btn :disabled="!filter" @click="filter = ''">Effacer</b-btn>
                    </b-input-group-append>
                  </b-input-group>
                </b-form-group>
              </b-col>
            </b-row>
            <br />
            <b-table striped :items="com" :fields="fields2" :filter="filter" :current-page="currentPage2" :per-page="perPage">
              <template slot="modifierDroits" slot-scope="row">
                <b-btn type="button" class="btn-info" v-on:click="getStudent(row.item.id)" v-b-modal="'changeState'"><i class="fas fa-edit"></i></b-btn>
              </template>
            </b-table>
            <b-row v-if="com.length > 0">
              <div class="center-block">
                <b-pagination :total-rows="com.length" :per-page="perPage" v-model="currentPage2" class="my-0" />
              </div>
            </b-row>
          </b-container>

          <b-modal id="changeState">
            <form v-on:submit.prevent="updateStudent()">
              <b-form-group label="Droit de l'utilisateur">
                <select v-model="currentStudent.status">
                  <option>admin</option>
                  <option>com</option>
                  <option>mvp</option>
                  <option>etudiant</option>
                </select>
              </b-form-group>
              <div class="modal-footer">
                <button type="submit" class="btn btn-primary">Save changes</button>
              </div>
            </form>
          </b-modal>

          <b-container>
            <h2 class="titre">MVP</h2>
            <hr class="style-four">
            <b-row>
              <b-col sm="6" offset="3">
                <b-form-group horizontal label="Filtrer :" class="mb-0">
                  <b-input-group>
                    <b-form-input v-model="filter2" placeholder="Rechercher un membre CRISTAL" />
                    <b-input-group-append>
                      <b-btn :disabled="!filter2" @click="filter2 = ''">Effacer</b-btn>
                    </b-input-group-append>
                  </b-input-group>
                </b-form-group>
              </b-col>
            </b-row>
            <br />
            <b-table striped :items="mvp" :fields="fields2" :filter="filter2" :current-page="currentPage3" :per-page="perPage">
              <template slot="modifierDroits" slot-scope="row">
                <b-btn type="button" class="btn-info" v-on:click="getStudent(row.item.id)" v-b-modal="'changeState'"><i class="fas fa-edit"></i></b-btn>
              </template>
            </b-table>
            <b-row v-if="mvp.length > 0">
              <div class="center-block">
                <b-pagination :total-rows="mvp.length + 1" :per-page="perPage" v-model="currentPage3" class="my-0" />
              </div>
            </b-row>
          </b-container>
          <b-container>
            <h2 class="titre">Prestataire</h2>
            <hr class="style-four">
            <b-row>
              <b-col sm="6" offset="3">
                <b-form-group horizontal label="Filtrer :" class="mb-0">
                  <b-input-group>
                    <b-form-input v-model="filter3" placeholder="Rechercher un membre CRISTAL" />
                    <b-input-group-append>
                      <b-btn :disabled="!filter3" @click="filter3 = ''">Effacer</b-btn>
                    </b-input-group-append>
                  </b-input-group>
                </b-form-group>
              </b-col>
            </b-row>
            <br />
            <b-table striped :items="eleve" :fields="fields2" :filter="filter3" :current-page="currentPage4" :per-page="perPage">
              <template slot="modifierDroits" slot-scope="row">
                <b-btn type="button" class="btn-info" v-on:click="getStudent(row.item.id)" v-b-modal="'changeState'"><i class="fas fa-edit"></i></b-btn>
              </template>
            </b-table>
            <b-row v-if="eleve.length > 0">
              <div class="center-block">
                <b-pagination :total-rows="eleve.length + 1" :per-page="perPage" v-model="currentPage4" class="my-0" />
              </div>
            </b-row>
          </b-container>
        </b-container>
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
/* eslint-disable new-cap */
import Nav from '../Nav'
import Footer from '../Footer'
import axios from 'axios'
import jsPDF from 'jsPDF'
export default {
  name: 'ProfilAdmin_profil',
  components: {Footer, Nav},
  data () {
    return {
      students: [],
      currentStudent: [],
      fields: [
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
          key: 'email',
          sortable: false
        }
      ],
      fields2: [
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
          key: 'email',
          sortable: false
        },
        {
          key: 'modifierDroits',
          label: 'Modifier les droits'
        }
      ],
      com: [],
      mvp: [],
      admin: [],
      eleve: [],
      filter: null,
      filter1: null,
      filter2: null,
      filter3: null,
      loading: false,
      currentPage: 1,
      currentPage1: 1,
      currentPage2: 1,
      currentPage3: 1,
      currentPage4: 1,
      perPage: 5
    }
  },
  mounted: function () {
    this.test()
    this.getStudents()
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
    createPDF () {
      let pdfName = 'membres-cristal'
      var doc = new jsPDF()

      doc.text('MEMBRES DE CRISTAL', 10, 10)
      doc.text('ADMINISTRATEURS', 10, 20)
      doc.text('Nom', 70, 20)
      doc.text('Prénom', 110, 20)

      var i = 0
      for (i; i < this.admin.length; i++) {
        doc.text(this.admin[i].lastname, 70, 30 + i * 10)
        doc.text(this.admin[i].firstname, 110, 30 + i * 10)
      }
      doc.text('COMMERCIAUX', 10, 30 + i * 10)
      i++
      for (var j = 0; j < this.com.length; j++) {
        doc.text(this.com[j].lastname, 70, (30 + i * 10) + j * 10)
        doc.text(this.com[j].firstname, 110, (30 + i * 10) + j * 10)
      }

      doc.save(pdfName + '.pdf')
    },
    getStudents: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/etudiant/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.students = response.data
          this.loading = false
          this.sortStudents(this.students)
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    sortStudents: function (students) {
      for (var i = 0; i < students.length; i++) {
        if (students[i].status === 'com') {
          this.com.push(students[i])
        } else if (students[i].status === 'mvp') {
          this.mvp.push(students[i])
        } else if (students[i].status === 'admin') {
          this.admin.push(students[i])
        } else {
          this.eleve.push(students[i])
        }
      }
    },
    getStudent: function (id) {
      this.loading = true
      let apiUrl = `http://127.0.0.1:8000/api/etudiant/${id}/`
      axios.get(apiUrl)
        .then((response) => {
          this.currentStudent = response.data
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    updateStudent: function () {
      this.loading = true
      let apirUrl = `http://127.0.0.1:8000/api/etudiant/${this.currentStudent.id}/`
      axios.put(apirUrl, this.currentStudent)
        .then((response) => {
          this.loading = false
          this.currentStudent = response.data
          this.getStudents()
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
  .center-block {
    margin-left:auto;
    margin-right:auto;
    display:block;
  }
</style>
