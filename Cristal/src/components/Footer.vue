<template>
  <div id="footer">
    <b-container fluid>
      <b-row>
        <b-col sm="4">
          <b-row>
            <table style="height: 100px;">
              <tbody>
              <tr>
                <td style="width: 20%; text-align: center;">
                  <img src="../assets/epita_white.png" class="img-responsive center-block" id="epita" alt="logo EPITA" />
                </td>
                <td style="width: 1%"></td>
                <td class="align-middle" style="width: 70%; text-align: justify"><p>
                  <br/>
                  École pour l’informatique et les techniques avancées depuis 1984. Diplôme d’Ingénieur habilité par la
                  CTI et certifié Label EUR-ACE. Titre d'expert enregistré au RNCP et certifié par l’Etat niveau 1.
                  Diplôme national de master en sciences et technologies mention « informatique ».</p>
                </td>
              </tr>
              </tbody>
            </table>
          </b-row>
        </b-col>
        <b-col sm="4" class="text-center">
          <img src="../assets/logo-cristal-blanche.png" id="cristal" alt="Logo Cristal"/>
          <p class="text-center">
            Campus Numérique Paris Sud <br />
            14-16 Rue Voltaire <br />
            94270 Le Kremlin-Bicêtre, France
            <br />
            Téléphone : +33 (0)1 46 71 54 79
            <br />
            Courriel : <a id="mail" href="mailto:contact@cristal.je">contact@cristal.je</a>
          </p>
        </b-col>
        <b-col sm="4">
          <google-map />
        </b-col>
      </b-row>
      <p style="font-size: small; text-align: center">Copyright Cristal 2018 - Tous droits réservé</p>
    </b-container>
  </div>
</template>

<script>
import GoogleMap from './GoogleMap'

export default {
  name: 'Footer',
  components: {
    GoogleMap
  }
}
</script>

<style scoped>
  #footer {
    margin-top: 40px;
    background-color: #3E4857;
    bottom: 0;
    padding-bottom: 5px;
    padding-top: 40px;
    color: white;
    padding-left: 2%;
    padding-right: 2%;;
  }
  #epita {
    width: 100px;
    height: auto;
  }
  #cristal {
    width: 70px;
    height: auto;
  }
  #mail{
    color: #79b249;
  }
</style>
