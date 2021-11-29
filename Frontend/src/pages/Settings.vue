<template v-if="isAuth">
  <h1 class="h1-text">Настройки</h1>
  <div class="container">
    <div class="row">
      <change-password-form></change-password-form>
    </div>
    <div class="row">
      <change-email-form></change-email-form>
    </div>
    <div class="row">
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
import ChangePasswordForm from "../components/ChangePasswordForm";
import NotificationForm from "../components/NotificationForm";
import ChangeEmailForm from "../components/ChangeEmailForm";
export default {
  name: "Settings",
  components: {
    ChangePasswordForm,
    NotificationForm,
    ChangeEmailForm,
  },
  methods: {
    ...mapMutations({
      setAuth: 'auth/setAuth'
    }),
    logout() {
      this.setAuth(false)
      localStorage.clear();
      this.$router.push({ name: 'auth' });
    }
  },
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth
    }),
  }
}
</script>

<style scoped>

</style>