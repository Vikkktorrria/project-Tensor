<template>
  <h1 class="h1-text">Настройки</h1>
  <div class="container">
    <div class="row">
      <change-password-form></change-password-form>
    </div>
    <div class="row">
      <change-email-form></change-email-form>
    </div>
    <div class="row" v-if="!currentUser.isDoctor">
      <notification-form></notification-form>
    </div>

  </div>
  <div class="form__button">
    <button
        class="btn"
        @click="logout"
    >
      Выйти
    </button>
  </div>
</template>

<script>
import {mapMutations, mapState} from 'vuex';
import ChangePasswordForm from "../components/Settings/ChangePasswordForm";
import NotificationForm from "../components/Settings/NotificationForm";
import ChangeEmailForm from "../components/Settings/ChangeEmailForm";
export default {
  name: "Settings",
  components: {
    ChangePasswordForm,
    NotificationForm,
    ChangeEmailForm,
  },
  methods: {
    ...mapMutations({
      setAuth: 'auth/setAuth',
    }),
    logout() {
      this.setAuth(false)
      localStorage.clear();
      this.$router.push({ name: 'auth' });
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
      isAuth: state => state.auth.isAuth,
    }),
  },
}
</script>

<style scoped>

</style>