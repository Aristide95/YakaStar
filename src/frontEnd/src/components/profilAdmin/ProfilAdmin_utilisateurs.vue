<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
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
            <b-col sm="4" offset="4">
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
          <b-table striped :items="admin" :fields="fields" :filter="filter1">
            <template slot="Modifier" slot-scope="row">
            </template>
          </b-table>
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
          <b-table striped :items="com" :fields="fields2" :filter="filter">
            <template slot="modifierDroits" slot-scope="row">
              <b-btn type="button" class="btn-info" v-on:click="getStudent(row.item.id)" v-b-modal="'changeState'"><i class="fas fa-edit"></i></b-btn>
            </template>
          </b-table>
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
          <b-table striped :items="mvp" :fields="fields2" :filter="filter2">
            <template slot="modifierDroits" slot-scope="row">
              <b-btn type="button" class="btn-info" v-on:click="getStudent(row.item.id)" v-b-modal="'changeState'"><i class="fas fa-edit"></i></b-btn>
            </template>
          </b-table>
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
          <b-table striped :items="eleve" :fields="fields2" :filter="filter3">
            <template slot="modifierDroits" slot-scope="row">
              <b-btn type="button" class="btn-info" v-on:click="getStudent(row.item.id)" v-b-modal="'changeState'"><i class="fas fa-edit"></i></b-btn>
            </template>
          </b-table>
        </b-container>
      </b-container>
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
      loading: false
    }
  },
  mounted: function () {
    this.getStudents()
  },
  methods: {
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
