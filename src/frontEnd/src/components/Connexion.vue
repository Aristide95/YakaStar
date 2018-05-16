<template>
    <div class="co">
      <Nav></Nav>
      <b-container class="connexion">
        <h1 class="titre">Connexion</h1>
        <hr class="style-four">
        <div class="inner">
          <b-col sm="4" offset="4">
            <b-form v-on:submit.prevent="connexion()" v-if="show">
              <b-form-group label="Login :">
                <b-form-input type="text" v-model="form.login" required placeholder="login_x"></b-form-input>
              </b-form-group>
              <b-form-group label="Mot de passe :">
                <b-form-input type="password" v-model="form.psw" required placeholder="*******"></b-form-input>
              </b-form-group>
              <div class="text-center">
                <b-button id="submit" type="submit" variant="primary">Se connecter</b-button>
              </div>
            </b-form>
          </b-col>
        </div>
      </b-container>
      <Footer></Footer>
    </div>
</template>

<script>
import Nav from './Nav'
import Footer from './Footer'
import axios from 'axios'

export default {
  name: 'Connexion',
  components: {Footer, Nav},
  data () {
    return {
      show: true,
      form: {
        login: null,
        psw: null
      }
    }
  },
  methods: {
    connexion: function () {
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
    }
  }
}
</script>

<style scoped>
  .inner {
    height: 47vh;
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
</style>
