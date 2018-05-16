<template>
  <div class="profil">
    <Nav></Nav>
    <b-nav justified tabs>
      <b-nav-item active>Profil</b-nav-item>
      <b-nav-item>Statistiques</b-nav-item>
      <b-nav-item>Missions</b-nav-item>
      <b-nav-item>Gestion des missions</b-nav-item>
      <b-nav-item>Gestion des utilisateurs</b-nav-item>
      <b-container></b-container>
    </b-nav>
    <Footer></Footer>
  </div>
</template>

<script>
import Nav from './Nav';
import Footer from './Footer';
export default {
  name: 'ProfilAdmin',
  components: {Footer, Nav}
}
</script>

<style scoped>

</style>
