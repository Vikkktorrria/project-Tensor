<template>
  <nav
       :class="{
          'navigation col-lg-2 active': burgerIsActive,
          'navigation col-lg-2': !burgerIsActive
        }"
    >
    <div
        :class="{
          'navigation__burger active': burgerIsActive,
          'navigation__burger': !burgerIsActive,
        }"
        @click="changeNav"
    >
      <div class="navigation__line"></div>
      <div class="navigation__line"></div>
      <div class="navigation__line"></div>
    </div>
    <div class="navigation__bar" v-if="isAuth">
      <nav-el
          @click="$router.push('/profile')"
          :is-active="isSelected('/profile')"
          :class-icon="'user-icon'"
      >Профиль</nav-el>
      <nav-el
          @click="$router.push('/notification')"
          :is-active="isSelected('/notification')"
          :class-icon="'notification-icon'"
      >Уведомления</nav-el>
      <nav-el
          @click="$router.push('/settings')"
          :is-active="isSelected('/settings')"
          :class-icon="'settings-icon'"
      >Настройки</nav-el>
    </div>
    <div class="navigation__bar" v-if="!isAuth">
      <nav-el
          @click="$router.push('/registration')"
          :is-active="isSelected('/registration')"
          :class-icon="'registration-icon'"
      >Регистрация</nav-el>
      <nav-el
          @click="$router.push('/auth')"
          :is-active="isSelected('/auth')"
          :class-icon="'auth-icon'"
      >Войти</nav-el>
      <nav-el
          @click="$router.push('/question')"
          :is-active="isSelected('/question')"
          :class-icon="'question-icon'"
      >Помощь</nav-el>
    </div>
  </nav>
</template>

<script>
import NavEl from "./NavEl";
import {mapState} from 'vuex';
export default {
  components: {
    NavEl
  },
  name: "NavbarAuth",
  data() {
    return {
      burgerIsActive: false
    }
  },
  methods: {
    isSelected(href) { return this.$route.href === href },
    changeNav() {
      console.log('click')
      this.burgerIsActive = !this.burgerIsActive
    }
  },
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth,
    }),
  },
}
</script>

<style lang="scss" src="@/assets/style/style.scss" scoped>
.row {
  padding-top: 20px;
}
</style>