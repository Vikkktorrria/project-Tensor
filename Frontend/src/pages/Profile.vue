<template>
  <div class="container">
    <div class="row">
      <div class="card card_user col-2">
        <img class="card_user__image" src="../assets/image/user-icon.png" alt="Татьяна">
      </div>
      <div class="card card_no-border col-md-8">
        <div class="card__title">
          {{currentUser.name}}
        </div>
        <div class="card__text">
          {{currentUser.age}} лет
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="row">
      <passport-form></passport-form>
      <snils-form></snils-form>
    </div>
  </div>
  <div class="container">
    <div class="row">
      <anamnesis-form></anamnesis-form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PassportForm from "../components/PassportForm";
import SnilsForm from "../components/SnilsForm";
import AnamnesisForm from "../components/AnamnesisForm";
import {mapState} from "vuex";
export default {
  name: "Profile",
  components: {
    PassportForm,
    SnilsForm,
    AnamnesisForm
  },
  data() {
    return {
      age: ''
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser
    })
  },
  methods: {
  },

}
</script>

<style scoped>
</style>