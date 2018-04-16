<template>
    <div class="competence">
      <Nav></Nav>
      <b-container fluid id="header">
      </b-container>
      <b-container>
        <h1 class="titre">A votre service pour trouver des solutions !</h1>
        <hr class="style-four">
        <p style="text-align: justify">
          Cristal vous propose des prestations couvrant tout type de besoin informatique. L'internet, le multimédia, la
          sécurité, les réseaux, les systèmes d'information, les bases de données sont autant de domaines où nous sommes
          susceptible d'intervenir, et ceci du conseil jusqu'au développement.
        </p>
        <p style="text-align: justify">
          Toutefois nos services ne s'arrêtent pas là, la richesse des profils des étudiants de l'Epita nous permet
          d'offrir une gamme de prestations inégalée, aussi bien pour des technologies ayant fait leurs preuves que pour
          les nouveautés du marché.
        </p>
      </b-container>
      <b-container fluid id="gris">
        <h2 class="titre">Nos garanties</h2>
        <b-container>
          <hr class="style-four">
          <div class="grid-3">
            <div class="jumbotron1">
              <div class="text-center" style="font-size:3em; color:#79b249"><i class="fas fa-chart-line"></i></div>
              <h5 CLASS="" style="text-align: center">Compétitivité</h5>
              <p style="text-align: center">Cristal propose des tarifs avantageux en comparaison de ceux pratiqués par
                les Sociétés de Service en Ingénierie Informatique tout en offrant une haute qualification des
                intervenants.</p>
            </div>
            <div class="jumbotron1">
              <div class="text-center" style="font-size:3em; color:#79b249"><i class="fas fa-graduation-cap"></i></div>
              <h5 style="text-align: center">Formation</h5>
              <p style="text-align: center">Les formations de l'école EPITA garantie des connaissances techniques
                avancées et une forte adaptabilité de la part des prestataires.</p>
            </div>
            <div class="jumbotron1">
              <div class="text-center" style="font-size:3em; color:#79b249"><i class="fas fa-code"></i></div>
              <h5 style="text-align: center">Téchnologies</h5>
              <p style="text-align: center">Nous maîtrisons tous types de besoins informatique, des technologies les
                plus répandues jusqu'aux plus confidentielles, du conseil jusqu'à l'intégration : réseaux, base de
                données, développement internet et mobile, multimédia.</p>
            </div>
          </div>
        </b-container>
      </b-container>
      <b-container>
        <h2 class="titre">Domaines et compétences</h2>
        <hr class="style-four">
        <p style="text-align: justify">Nous maîtrisons tous types de besoins informatique, des technologies les plus
          répandues jusqu'aux plus confidentielles, du conseil jusqu'à l'intégration : réseaux, base de données,
          développement internet et mobile, multimédia.
        </p>
        <b-col sm="8" offset="2">
          <div class="grid-3">
            <div class="jumbotron">
              <div class="text-center" style="font-size:2em; color:#79b249"><i class="fas fa-laptop"></i></div>
              <h5 CLASS="" style="text-align: center">Web</h5>
              <p style="text-align: center">Site vitrine, E-commerce, Réseaux sociaux, Intranet/Extranet, ...</p>
            </div>
            <div class="jumbotron">
              <div class="text-center" style="font-size:2em; color:#79b249"><i class="fas fa-mobile-alt"></i></div>
              <h5 style="text-align: center">Mobile</h5>
              <p style="text-align: center">Android, IOS, Windows Phone, Blackberry, Bada, ...</p>
            </div>
            <div class="jumbotron">
              <div class="text-center" style="font-size:2em; color:#79b249"><i class="far fa-chart-bar"></i></div>
              <h5 style="text-align: center">Applicatif</h5>
              <p style="text-align: center">Windows, Mac OS, Unix, Office, ...</p>
            </div>
          </div>
        </b-col>
        <b-col sm="8" offset="2">
          <div class="grid-3">
            <div class="jumbotron">
              <div class="text-center" style="font-size:2em; color:#79b249"><i class="fas fa-cogs"></i></div>
              <h5 CLASS="" style="text-align: center">Administration</h5>
              <p style="text-align: center">Office 365, Serveur, Architecture, ...</p>
            </div>
            <div class="jumbotron">
              <div class="text-center" style="font-size:2em; color:#79b249"><i class="fas fa-lock"></i></div>
              <h5 style="text-align: center">Sécurité</h5>
              <p style="text-align: center">Prévention, Pentesting, Analyse de risque, Post-incident, ...</p>
            </div>
            <div class="jumbotron">
              <div class="text-center" style="font-size:2em; color:#79b249"><i class="fas fa-cloud"></i></div>
              <h5 style="text-align: center">Réseau & Télécom</h5>
              <p style="text-align: center">Cloud computing, Infrastructure, VOIP, Téléphonie, Hébergement, ...</p>
            </div>
          </div>
        </b-col>
        <h3 style="text-align: center; color: #0c365a">• AUDIT • CONSEIL • R&D • FORMATION • SUPPORT •</h3>
      </b-container>
      <Footer></Footer>
    </div>
</template>

<script>
import Nav from './Nav'
import Footer from './Footer'
export default {
  name: 'Competence',
  components: {Footer, Nav}
}
</script>

<style scoped>
  #header {
    height: 50vh;
    background: url('../assets/cristal_mac.png') no-repeat;
    background-size: cover;
  }
  hr.style-four {
    height: 12px;
    border: 0;
    box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);
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
    padding-bottom: 20px;
    padding-top: 20px;
  }
  .jumbotron1 {
    background-color: #F5F7F9;
    border: 1px solid #ddd;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
    padding-bottom: 20px;
    padding-top: 20px;
    border-radius: 5px;
  }
  .titre{
    color: #0c365a;
    text-align: center;
    padding-top: 30px;
    padding-bottom: 20px;
  }
  #gris {
    margin-top: 50px;
    background-color: #F5F7F9;
    padding-bottom: 50px;
  }
</style>
