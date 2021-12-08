<template>
  <div v-if="!currentUser.isDoctor" class="container">
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
import {mapState} from "vuex";
import PassportForm from "./PassportForm";
import SnilsForm from "./SnilsForm";
import AnamnesisForm from "./AnamnesisForm";

export default {
  name: "ProfilePatient",
  components: {
    PassportForm,
    SnilsForm,
    AnamnesisForm
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
    }),
  },
}
</script>

<style scoped>

</style>