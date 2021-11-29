<template>
  <div class="container">
    <head-profile></head-profile>
  </div>
  <div class="container">
    <div class="row">
      <passport-form
          :current-user="currentUser"
      ></passport-form>
      <snils-form
          :current-user="currentUser"
      ></snils-form>
    </div>
  </div>
  <div class="container">
    <div class="row">
      <anamnesis-form
          :current-user="currentUser"
      ></anamnesis-form>
    </div>
  </div>
</template>

<script>
import PassportForm from "../components/PassportForm";
import SnilsForm from "../components/SnilsForm";
import AnamnesisForm from "../components/AnamnesisForm";
import HeadProfile from "../components/HeadProfile";
import {mapState} from "vuex";
export default {
  name: "Profile",
  components: {
    HeadProfile,
    PassportForm,
    SnilsForm,
    AnamnesisForm
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
      isAuth: state => state.auth.isAuth
    }),
  },
}
</script>

<style scoped>
</style>