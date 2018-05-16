<template>
  <div id="nav">
    <div id="fixe">
      <b-container fluid>
        <b-navbar toggleable="md">

          <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

          <b-navbar-brand href="#"><router-link :to="{name: 'Accueil'}">
            <img class="logo" src="../assets/logo.png" alt="Logo Cristal" />
          </router-link></b-navbar-brand>

          <b-container>
            <b-collapse is-nav id="nav_collapse">

              <b-navbar-nav>
                <b-nav-item href="#"><router-link :to="{name: 'Accueil'}">Accueil</router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{name: 'Equipe'}">Équipe</router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{name: 'Services'}">Services</router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{name: 'Fonctionnement'}">Fonctionnement</router-link></b-nav-item>
              </b-navbar-nav>

              <!-- Right aligned nav items -->
              <b-navbar-nav class="ml-auto">
                <b-nav-item right href="#"><router-link :to="{name: 'Connexion'}">Connexion</router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{name: 'Contact'}">Contact</router-link></b-nav-item>
              </b-navbar-nav>

            </b-collapse>
          </b-container>
        </b-navbar>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Nav',
  show: true,
  form: {
    login: null,
    psw: null
  }
}
</script>

<style scoped>
  .logo{
    max-width: 125px;
    height: auto;
  }
  #fixe {
    overflow: hidden;
    position: fixed;
    top: 0;
    width: 100%;
    background-color: white;
    z-index: 100;
  }
  #nav {
    padding-bottom: 80px;
  }
  a {
    text-decoration: none;
    color: rgba(0, 0, 0, 0.5);
  }
  a:hover, a:focus {
    color: #0c365a;
  }
  a:active {
    color: #79b249;
  }
</style>
