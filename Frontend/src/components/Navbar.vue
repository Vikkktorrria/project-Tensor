<template>
  <nav class="navigation active col-lg-2">
    <div class="navigation__burger active">
      <div class="navigation__line"></div>
      <div class="navigation__line"></div>
      <div class="navigation__line"></div>
    </div>
    <div class="navigation__bar">
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
export default {
  components: {
    NavEl
  },
  name: "NavbarAuth",
  methods: {
    isSelected(href) { return this.$route.href === href }
  },
}
</script>

<style lang="scss" src="@/assets/style/style.scss">

</style>