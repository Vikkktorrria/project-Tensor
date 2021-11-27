<template>
  <div class="container-wrapper container">
    <header class="head head_center" v-if="!isAuth">
      <div class="logo">
        <img src="@/assets/image/logo.png" alt="MedCard">
        <a class="phone" href="tel:+73452564276">+ 7 3452 <span class="phone_bold">564-276</span></a>
      </div>
    </header>
    <header class="head" v-if="isAuth">
      <div class="logo">
        <img src="./assets/image/logo.png" alt="MedCard">
        <a class="phone" href="tel:+73452564276">+ 7 3452 <span class="phone_bold">564-276</span></a>
      </div>
      <div class="name">
        <div class="name__text">
          Здравствуйте, {{ this.currentUser.name }}!
        </div>
        <div class="name__icon">

        </div>
      </div>
    </header>
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
import {mapMutations, mapActions, mapState} from 'vuex';
export default {
  components: {
    Navbar, FooterComponent
  },
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth,
      currentUser: state => state.auth.currentUser
    })
  },
  methods: {
    ...mapMutations({
      setAuth: 'auth/setAuth',
    }),
    ...mapActions({
      userData: 'auth/userData',
    }),
    checkAuth() {
      if(localStorage.getItem('token')) {
        this.setAuth(true)
        this.userData()
      } else {
        this.setAuth(false)
      }
    }
  },
  mounted() {
    this.checkAuth()
  }
}
</script>

<style lang="scss" src="@/assets/style/style.scss">
</style>
