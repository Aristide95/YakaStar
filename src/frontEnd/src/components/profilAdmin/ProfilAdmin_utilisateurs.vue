<template>
  <div class="profil">
    <Nav></Nav>
    <b-container>
      <br />
      <b-nav justified tabs>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_profil'}">Profil</router-link></b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_statistique'}">Statistiques</router-link></b-nav-item>
        <b-nav-item> Mes missions</b-nav-item>
        <b-nav-item><router-link :to="{name: 'ProfilAdmin_missions'}">Gestion des missions</router-link></b-nav-item>
        <b-nav-item active>Gestion des utilisateurs</b-nav-item>
        <b-container>
          <h1 class="titre">Utilisateurs</h1>
          <hr class="style-four">
          <b-container>
            <h2 class="titre">Membre de CRISTAL</h2>
            <hr class="style-four">
            <b-table striped :items="admin" :fields="fields">
              <template slot="Modifier" slot-scope="row">
              </template>
            </b-table>
            <b-btn class="btn-info">Exporter</b-btn>
          </b-container>
          <b-container>
            <h2 class="titre">Commercial de CRISTAL</h2>
            <hr class="style-four">
            <b-table striped :items="com" :fields="fields"></b-table>
          </b-container>
          <b-container>
            <h2 class="titre">MVP</h2>
            <hr class="style-four">
            <b-table striped :items="mvp" :fields="fields"></b-table>
          </b-container>
          <b-container>
            <h2 class="titre">Prestataire</h2>
            <hr class="style-four">
            <b-table striped :items="eleve" :fields="fields"></b-table>
          </b-container>
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
export default {
  name: 'ProfilAdmin_profil',
  components: {Footer, Nav},
  data () {
    return {
      students: [],
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
      com: [],
      mvp: [],
      admin: [],
      eleve: [],
      loading: false
    }
  },
  mounted: function () {
    this.getStudent()
  },
  methods: {
    getStudent: function () {
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
    getCom: function () {
      let apirUrl = 'http://127.0.0.1:8000/api/etudiant/'
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.com = response.data
          var i = 0
          for (var s in this.students) {
            if (s.status !== 'com') {
              this.com = this.com.splice(i, 1)
            }
            i = i + 1
          }
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
</style>
