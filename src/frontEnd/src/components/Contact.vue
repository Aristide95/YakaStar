<template>
    <div id="contact">
      <Nav></Nav>
      <b-container fluid id="gris">
        <b-container>
          <h1 class="titre">Un projet, une envie ? Contactez-nous :</h1>
          <hr class="style-four">
          <div>
            <b-col sm="6" offset="3" id="formulaire">
              <b-form @submit="onSubmit" v-if="show">
                <b-form-group id="exampleInputGroup1"
                              label="Nom et prénom"
                              label-for="exampleInput1">
                  <b-form-input id="exampleInput1"
                                type="text"
                                v-model="form.nom"
                                required
                                placeholder="Obligatoire">
                  </b-form-input>
                </b-form-group>
                <b-form-group id="exampleInputGroup2"
                              label="Adresse mail"
                              label-for="exampleInput2">
                  <b-form-input id="exampleInput2"
                                type="email"
                                v-model="form.email"
                                required
                                placeholder="Obligatoire">
                  </b-form-input>
                </b-form-group>
                <b-form-group id="exampleInputGroup3"
                              label="Société"
                              label-for="exampleInput3">
                  <b-form-input id="exampleInput2"
                                type="text"
                                v-model="form.society"
                                required
                                placeholder="Obligatoire">
                  </b-form-input>
                </b-form-group>
                <b-form-group id="exampleInputGroup4"
                              label="Téléphone"
                              label-for="exampleInput4">
                  <b-form-input id="exampleInput1"
                                type="tel"
                                v-model="form.phone"
                                required
                                placeholder="Obligatoire">
                  </b-form-input>
                </b-form-group>
                <b-form-group id="exampleInputGroup5"
                              label="Message"
                              label-for="exampleInput5">
                  <b-form-textarea id="textarea1"
                                   v-model="form.message"
                                   placeholder="Obligatoire"
                                   :rows="3"
                                   :max-rows="6"
                                   required >
                  </b-form-textarea>
                </b-form-group>
                <b-form-group id="exampleInputGroup5"
                              label="Pièce jointe (Max 10Mo - .zip/.jpg/.pdf)"
                              label-for="exampleInput5">
                  <b-form-file accept=".jpg, .pdf, .zip" v-model="form.p1" class="mt-3" plain></b-form-file>
                  <b-form-file accept=".jpg, .pdf, .zip" v-model="form.p2" class="mt-3" plain></b-form-file>
                  <b-form-file accept=".jpg, .pdf, .zip" v-model="form.p3" class="mt-3" plain></b-form-file>
                </b-form-group>
                <div class="text-center">
                  <b-button id="submit" type="submit" variant="primary">Envoyer</b-button>
                </div>
              </b-form>
            </b-col>
          </div>
        </b-container>
      </b-container>
      <b-container>
        <b-row>
          <b-col sm="6">
            <h2 class="titre">Adresse</h2>
            <hr class="style-four">
            <p class="text-center">14-16 Rue Voltaire<br />
              94270 Le Kremlin-Bicêtre, France</p>
          </b-col>
          <b-col sm="6">
            <h2 class="titre">Contact</h2>
            <hr class="style-four">
            <p class="text-center">+33.1.46.71.54.79<br />
              contact@cristal.je</p>
          </b-col>
        </b-row>
      </b-container>
      <Footer></Footer>
    </div>
</template>

<script>
import Nav from './Nav'
import Footer from './Footer'
export default {
  name: 'Contact',
  components: {Footer, Nav},
  data () {
    return {
      form: {
        email: '',
        nom: '',
        society: '',
        message: '',
        phone: '',
        p1: null,
        p2: null,
        p3: null
      },
      show: true
    }
  }
}
</script>

<style scoped>
  #formulaire {
    margin-top: 70px;
    margin-bottom: 40px;
    border: 1px solid #F5F8F9;
    background-color: white;
    padding: 30px;
    border-radius: 10px;
  }
  #gris {
    background-color: #F5F7F9;
    padding-bottom: 40px;
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
  #submit {
    background-color: #79b249;
    border-color: #598236;
  }
</style>
