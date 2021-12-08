<template>
  <div class="container-wrapper container">
    <header-component></header-component>
    <div class="article row">
      <navbar></navbar>
      <section class="content col-lg-8">
        <router-view></router-view>
        <footer-component></footer-component>
      </section>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar";
import 'bootstrap/dist/css/bootstrap.css'
import FooterComponent from "./components/FooterComponent";
import HeaderComponent from "./components/HeaderComponent";
import {mapMutations, mapActions, mapState} from 'vuex';
export default {
  components: {
    Navbar, FooterComponent, HeaderComponent
  },
}
</script>

<style lang="css" src="@/assets/style/style.css">
</style>
