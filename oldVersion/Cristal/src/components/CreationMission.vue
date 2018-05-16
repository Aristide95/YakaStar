<template>
  <div id="creation">
    <Nav></Nav>
    <b-container>
      <h1 class="titre">Création d'une mission</h1>
      <hr class="style-four">
      <b-col sm="6" offset="3" id="formulaire">
        <b-form @submit="onSubmit" v-if="show">
          <b-form-group label="Titre de la mission">
            <b-form-input type="text" v-model="form.titre" required placeholder="Obligatoire"></b-form-input>
          </b-form-group>
          <b-form-group label="Type de la mission">
            <select v-model="form.type">
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
            <b-form-input type="text" v-model="form.name" required placeholder="Obligatoire"></b-form-input>
          </b-form-group>
          <b-form-group label="Nombre de prestataires sur la mission">
            <b-form-input type="number" v-model="form.numpresta" required placeholder="Obligatoire"></b-form-input>
          </b-form-group>
          <b-form-group label="Description">
            <b-form-textarea v-model="form.desc" placeholder="Obligatoire"
                             :rows="3"
                             :max-rows="6"
                             required >
            </b-form-textarea>
          </b-form-group>
          <b-form-group label="Technologies de la mission">
            <input type="checkbox" id="android" value="android" v-model="checkedNames">
            <label for="android">Android</label>
            <input type="checkbox" id="ios" value="ios" v-model="checkedNames">
            <label for="ios">Ios</label>
            <input type="checkbox" id="vuejs" value="vuejs" v-model="checkedNames">
            <label for="vuejs">Vuejs</label>
            <input type="checkbox" id="java" value="java" v-model="checkedNames">
            <label for="java">Java</label>
            <input type="checkbox" id="django" value="django" v-model="checkedNames">
            <label for="django">Django</label>
            <input type="checkbox" id="php" value="php" v-model="checkedNames">
            <label for="php">PHP</label>
            <input type="checkbox" id="technoLibre" value="technoLibre" v-model="checkedNames">
            <label for="technoLibre">Techno libre</label>
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
export default {
  name: 'CreationEntreprise',
  components: {Footer, Nav},
  data () {
    return {
      form: {
        titre: '',
        name: '',
        numpresta: '',
        type: ''
      },
      show: true,
      file: null
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
