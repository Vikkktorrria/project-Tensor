<template>
  <header class="head head_center" v-if="!isAuth">
    <div class="logo">
      <img src="@/assets/image/logo.png" alt="MedCard">
      <a class="phone" href="tel:+73452564276">+ 7 3452 <span class="phone_bold">564-276</span></a>
    </div>
  </header>
  <header class="head" v-if="isAuth">
    <div class="logo">
      <img src="@/assets/image/logo.png" alt="MedCard">
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
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";

export default {
  name: "HeaderComponent",
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth,
      currentUser: state => state.auth.currentUser,
    })
  },
  methods: {
    ...mapMutations({
      setAuth: 'auth/setAuth',
    }),
    ...mapActions({
      checkAuth: 'auth/checkAuth'
    }),
  },
  mounted() {
    this.checkAuth()
  }
}
</script>

<style scoped>

</style>