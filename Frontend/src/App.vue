<template>
  <div class="container-wrapper container">
    <header class="head head_center">
      <div class="logo">
        <img src="@/assets/image/logo.png" alt="MedCard">
        <a class="phone" href="tel:+73452564276">+ 7 3452 <span class="phone_bold">564-276</span></a>
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
export default {
  components: {
    Navbar, FooterComponent
  }
}
</script>

<style lang="scss" src="@/assets/style/style.scss">
</style>
