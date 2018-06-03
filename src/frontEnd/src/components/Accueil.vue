<template>
  <div>
    <Nav></Nav>
    <b-container fluid id="header">
      <div class="text-center d-none d-sm-block">
        <h1 id="titre">LA JUNIOR DE L'INTELLIGENCE INFORMATIQUE</h1>
        <div class="text-center">
          <b-button id="contact" href="#/contact">CONTACTEZ NOUS</b-button>
        </div>
      </div>
      <div class="text-center d-block d-sm-none">
        <h1 id="titre1">LA JUNIOR DE L'INTELLIGENCE INFORMATIQUE</h1>
        <div class="text-center">
          <b-button id="contact" href="#/contact">CONTACTEZ NOUS</b-button>
        </div>
      </div>
    </b-container>
    <b-container>
      <h2 class="titre">À votre service pour trouver des solutions</h2>
      <hr class="style-four"/>
      <div class="d-none d-sm-block">
        <div class="grid-3">
          <div class="jumbotron">
            <div class="text-center" style="font-size:3em; color:#79b249"><i class="fas fa-quote-right"></i></div>
            <h5 CLASS="" style="text-align: center">Qui sommes nous ?</h5>
            <p style="text-align: justify">Formée d'étudiants volontaires, Cristal, l'Association Entreprise de l'école EPITA (École d'ingénieurs en
              informatique du pôle technologique IONIS), a pour vocation de compléter la formation des étudiants de
              l'école en leur faisant gagner de l'expérience professionnelle. Au service et à l'écoute de nos clients
              depuis 1989, nous fournissons des services de qualité adaptés à leurs besoins, et ce dans tous les domaines
              relatifs à l'informatique : conseil, conception et réalisation.</p>
          </div>
          <div class="jumbotron">
            <div class="text-center" style="font-size:3em; color:#79b249"><i class="fas fa-cogs"></i></div>
            <h5 style="text-align: center">Notre fonctionnement</h5>
            <p style="text-align: justify">Le fonctionnement de Cristal est semblable à celui d'une ESN (Entreprise de
              Services du Numérique). Elle propose aux sociétés qui en font la demande des prestations effectuées par des
              étudiants de l'école, leur permettant ainsi de découvrir le monde professionnel tout en complétant la
              formation qui leur est dispensée dans leur scolarité. Le rôle de l'association est de lier activement
              le client (la société), et le prestataire (l'étudiant).</p>
          </div>
          <div class="jumbotron">
            <div class="text-center" style="font-size:3em; color:#79b249"><i class="far fa-chart-bar"></i></div>
            <h5 style="text-align: center">Notre expérience</h5>
            <p style="text-align: justify">Forte d'une expérience de plus de 25 ans au service de l'entreprise, Cristal a
              su développer les processus nécessaires pour fournir des prestations de qualité, axés sur l'écoute des
              besoins du client, le conseil sur les nouvelles technologies et la sélection ciblée des profils. Chaque
              projet est unique, et nous nous appliquons à rechercher la solution la plus adaptée aux besoins exprimés,
              et ce en termes de performance, de complexité mais aussi de coût.</p>
          </div>
        </div>
      </div>
      <div class="d-block d-sm-none">
        <b-row xs="12">
          <div class="jumbotron">
            <div class="text-center" style="font-size:3em; color:#79b249"><i class="fas fa-quote-right"></i></div>
            <h5 CLASS="" style="text-align: center">Qui sommes nous ?</h5>
            <p style="text-align: justify">Formée d'étudiants volontaires, Cristal, l'Association Entreprise de l'école EPITA (École d'ingénieurs en
              informatique du pôle technologique IONIS), a pour vocation de compléter la formation des étudiants de
              l'école en leur faisant gagner de l'expérience professionnelle. Au service et à l'écoute de nos clients
              depuis 1989, nous fournissons des services de qualité adaptés à leurs besoins, et ce dans tous les domaines
              relatifs à l'informatique : conseil, conception et réalisation.</p>
          </div>
        </b-row>
        <b-row xs="12">
          <div class="jumbotron">
            <div class="text-center" style="font-size:3em; color:#79b249"><i class="fas fa-cogs"></i></div>
            <h5 style="text-align: center">Notre fonctionnement</h5>
            <p style="text-align: justify">Le fonctionnement de Cristal est semblable à celui d'une ESN (Entreprise de
              Services du Numérique). Elle propose aux sociétés qui en font la demande des prestations effectuées par des
              étudiants de l'école, leur permettant ainsi de découvrir le monde professionnel tout en complétant la
              formation qui leur est dispensée dans leur scolarité. Le rôle de l'association est de lier activement
              le client (la société), et le prestataire (l'étudiant).</p>
          </div>
        </b-row>
        <b-row xs="12">
          <div class="jumbotron">
            <div class="text-center" style="font-size:3em; color:#79b249"><i class="far fa-chart-bar"></i></div>
            <h5 style="text-align: center">Notre expérience</h5>
            <p style="text-align: justify">Forte d'une expérience de plus de 25 ans au service de l'entreprise, Cristal a
              su développer les processus nécessaires pour fournir des prestations de qualité, axés sur l'écoute des
              besoins du client, le conseil sur les nouvelles technologies et la sélection ciblée des profils. Chaque
              projet est unique, et nous nous appliquons à rechercher la solution la plus adaptée aux besoins exprimés,
              et ce en termes de performance, de complexité mais aussi de coût.</p>
          </div>
        </b-row>
      </div>
    </b-container>
    <b-container fluid id="gris">
      <h2 class="titre">Chiffres clés</h2>
      <b-container>
        <hr class="style-four">
        <b-row class="text-center">
          <b-col class="rond"><div style="padding-top: 15%;"><Count end="1989" /><span>Fondation</span></div></b-col>
          <b-col class="rond"><div style="padding-top: 15%;"><Count end="480" /><span>Chiffre d'affaire en M€</span></div></b-col>
          <b-col class="rond"><div style="padding-top: 15%;"><Count end="250" /><span>Projets annuels</span></div></b-col>
          <b-col class="rond"><div style="padding-top: 15%;"><Count end="4324" /><span>Étudiants</span></div></b-col>
        </b-row>
      </b-container>
    </b-container>
    <b-container>
      <h2 class="titre"><i class="fas fa-quote-left"></i> Témoignages <i class="fas fa-quote-right"></i></h2>
      <hr class="style-four">
      <div class="d-none d-sm-block">
        <b-row sm="12">
          <b-col sm="6">
            <b-row>
              <b-col sm="4">
                <img src="../assets/company/bnp.png" alt="logo BNP Paribas" class="img-thumbnail">
              </b-col>
              <b-col sm="8">
                <p style="font-size: small; text-align: justify">Grâce à leur réactivité et à leur souplesse, Cristal a su
                  s'adapter à nos contraintes et aux délais
                  serrés. Nous avons également pu apprécier leur professionnalisme dans la gestion du projet.</p>
              </b-col>
            </b-row>
          </b-col>
          <b-col sm="6">
            <b-row>
              <b-col sm="8">
                <p style="font-size: small; text-align: justify">Cristal a su m’apporter une solution sur mesure et
                  performante. Le professionnalisme dont mes différents interlocuteurs ont fait preuve nous a permis de
                  travailler dans des conditions optimales.</p>
              </b-col>
              <b-col sm="4">
                <img src="../assets/company/swarovski.png" alt="logo Swarovski" class="img-thumbnail">
              </b-col>
            </b-row>
          </b-col>
        </b-row>
        <b-row sm="12">
          <b-col sm="6" class="text-center" style="font-size: small">
            <span class="vert">L. Jeunhomme</span> - Responsable des Etudes Sectorielles
          </b-col>
          <b-col sm="6" class="text-center" style="font-size: small">
            <span class="vert">Anne-Charlotte Liegaux-Beucher</span> - Communication Analyst Manager
          </b-col>
        </b-row>
      </div>
      <b-row class="d-block d-sm-none">
        <b-row>
          <p style="font-size: small; text-align: center">Grâce à leur réactivité et à leur souplesse, Cristal a su
            s'adapter à nos contraintes et aux délais
            serrés. Nous avons également pu apprécier leur professionnalisme dans la gestion du projet.</p>
        </b-row>
        <b-row>
          <p class="text-center"><span class="vert">L. Jeunhomme</span> - Responsable des Etudes Sectorielles</p>
        </b-row>
        <b-row>
          <p style="font-size: small; text-align: center">Cristal a su m’apporter une solution sur mesure et
            performante. Le professionnalisme dont mes différents interlocuteurs ont fait preuve nous a permis de
            travailler dans des conditions optimales.</p>
        </b-row>
        <b-row>
          <p class="text-center"><span class="vert">Anne-Charlotte Liegaux-Beucher</span> - Communication Analyst Manager</p>
        </b-row>
      </b-row>
    </b-container>
    <b-container fluid>
      <h2 class="titre">Ils nous font confiance</h2>
      <hr class="style-four" />
      <carousel :per-page="6" :navigate-to="someLocalProperty" mouse-drag="false" class="d-none d-sm-block" style="margin-top: 50px">
        <slide class="text-center">
          <img src="../assets/company/adentis.png" alt="logo Adentis" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/swarovski.png" alt="logo Swarovski" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/medicapp.jpeg" alt="logo Medicapp" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/bnp.png" alt="logo BNP Paribas" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/century.png" alt="logo Century" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/grdf.png" alt="logo GRDF" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/eiffel.png" alt="logo Eiffel" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/sg.png" alt="logo Société Général" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/universite-de-geneve.gif" alt="logo Université de Genève" class="img-responsive logo"/>
        </slide>
      </carousel>
      <carousel :per-page="2" :navigate-to="someLocalProperty" mouse-drag="false" class="d-block d-sm-none" style="margin-top: 50px">
        <slide class="text-center">
          <img src="../assets/company/adentis.png" alt="logo Adentis" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/swarovski.png" alt="logo Swarovski" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/medicapp.jpeg" alt="logo Medicapp" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/bnp.png" alt="logo BNP Paribas" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/century.png" alt="logo Century" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/grdf.png" alt="logo GRDF" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/eiffel.png" alt="logo Eiffel" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/sg.png" alt="logo Société Général" class="img-responsive logo"/>
        </slide>
        <slide class="text-center">
          <img src="../assets/company/universite-de-geneve.gif" alt="logo Université de Genève" class="img-responsive logo"/>
        </slide>
      </carousel>
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Nav from './Nav.vue'
import Footer from './Footer.vue'
import Counter from './Count'
import axios from 'axios'

export default {
  components: {
    'Nav': Nav,
    'Footer': Footer,
    'Count': Counter
  },
  name: 'Accueil',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted: function () {
    this.test()
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
          this.getStudent(response.data['user_id']);
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
    getStudent: function (user_id) {
      let apirUrl = 'http://127.0.0.1:8000/api/etudiant/'+user_id
      this.loading = true
      axios.get(apirUrl)
        .then((response) => {
          this.student = response.data
          console.log(response.data)
          this.loading = false
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
  }
}
</script>

<style>
  #header {
    height: 50vh;
    background: url('../assets/accueil.jpg') no-repeat;
    background-size: cover;
  }
  #titre {
    vertical-align: middle;
    color: white;
    padding-top: 35vh;
    text-shadow: 2px 2px black;
  }
  #titre1 {
    vertical-align: middle;
    color: white;
    padding-top: 20vh;
    text-shadow: 2px 2px black;
  }
  .grid-3{
    padding-top: 20px;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
    -ms-flex-direction:row;
    flex-direction:row;
    -ms-flex-wrap:wrap;
    flex-wrap:wrap;
    margin-left:-30px;
    letter-spacing:-0.31em;
    text-rendering:optimizespeed;
  }
  .grid-3 > * {
    -webkit-box-flex:0;
    -ms-flex:0 0 auto;
    flex:0 0 auto;
    width:calc(33% - 30px);
    margin-left:30px;
    display:block;
    display:inline-block;
    vertical-align:top;
    letter-spacing:normal;
    text-rendering:auto;
  }
  .jumbotron {
    background-color: white;
    border: 1px solid #ddd;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
  }
  .titre{
    color: #0c365a;
    text-align: center;
    padding-top: 30px;
    padding-bottom: 20px;
  }
  hr.style-four {
    height: 12px;
    border: 0;
    box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);
  }
  #gris {
    background-color: #F5F7F9;
  }
  .rond {
    background-color: white;
    margin:2%;
    width:200px;
    height:200px;
    border-radius: 50%;
    -webkit-box-shadow: 3px 3px 15px 0px #DFE1E3;
    -moz-box-shadow: 3px 3px 15px 0px #DFE1E3;
    box-shadow: 3px 3px 15px 0px #DFE1E3;
  }
  .vert {
    color: #79b249;
  }
  .img-thumbnail {
    border: none;
  }
  .logo {
    vertical-align: middle;
    max-height: 10vh;
    max-width: 20vh;
  }
  #contact {
    background-color: #79b249;
    border-color: #598236;
  }
</style>
