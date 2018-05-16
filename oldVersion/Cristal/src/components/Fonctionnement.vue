<template>
  <div id="fonctionnement">
    <Nav></Nav>
    <b-container fluid id="header">
    </b-container>
    <b-container>
      <h2 class="titre">Notre fonctionnement</h2>
      <hr class="style-four"/>
      <b-row>
        <img src="../assets/fonctionnement.png" alt="image du fonctionnement Cristal" class="img-fluid"/>
      </b-row>
      <b-row>
        <p class="" style="text-align: justify; vertical-align: center; padding-top: 40px">
          Le fonctionnement de Cristal se rapproche de celui d'une ESN (Entreprise de Services du Numérique) et de
          celui d'une JE (Junior Entreprise).
          Elle propose aux sociétés qui en font la demande des prestations effectuées par des étudiants de l'Epita,
          leur permettant ainsi de découvrir le monde professionnel tout en complétant la formation qui leur est
          dispensée dans leur scolarité.
          Le rôle de l'association est de lier activement le client (la société), et le prestataire (l'étudiant) à
          travers un suivi régulier réalisé par nos ingénieurs d'affaires.
        </p>
      </b-row>
    </b-container>
    <b-container fluid>
      <div id="gris">
        <b-container style="padding-top: 50px">
          <b-row class="text-center">
            <b-col sm="6">
              <h3><i class="fas fa-building"></i> L'entreprise</h3>
              <hr class="style-four">
            </b-col>
            <b-col sm="6">
              <h3><i class="fas fa-graduation-cap"></i> L'étudiant</h3>
              <hr class="style-four">
            </b-col>
          </b-row>
          <b-row style="text-align: justify">
            <b-col sm="6">
              <p>
                Les entreprises nous transmettent leur besoin au travers d'un cahier des charges ou d'une proposition commerciale.
                Cristal se charge de diffuser la mission auprès des étudiants via ses différents canaux de communication.
                Une fois la sélection achevée, un point est effectué entre votre entreprise, l'étudiant et Cristal. Ce rendez-vous a pour objectif de répondre aux différentes questions des acteurs présents
                Une fois les modalités de contractualisation établie et acceptées, le commercial suit le bon déroulement de la mission en effectuant des points réguliers avec l'étudiant.
              </p>
            </b-col>
            <b-col sm="6">
              <p>
                Les étudiants de l'école Epita peuvent postuler aux missions dans le cadre de leur scolarité.
                S'ils sont intéressés par une mission, ils contactent les membres de l'association en témoignant de leur expertise au travers de leurs expériences professionnelles.
                Une fois ce contact établis et l'étudiant challengé, il étudie le projet avec le commercial en charge et formule les questions bloquantes qui seront ensuite présentées au client lors du premier rendez-vous.
                Une fois la mission débutée, l'étudiant est encadré par un membre de l'équipe Cristal qui se chargera de le guider tout en adoptant un avis critique vis-à-vis de l'ouvrage réalisé.
              </p>
            </b-col>
          </b-row>
        </b-container>
      </div>
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Footer from './Footer'
import Nav from './Nav'
export default {
  name: 'Fonctionnement',
  components: {Nav, Footer}
}
</script>

<style scoped>
  #header {
    height: 50vh;
    background: url('../assets/bandau.png') no-repeat;
    background-size: cover;
  }
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
  #gris {
    margin-top: 50px;
    background-color: #F5F7F9;
  }
</style>
