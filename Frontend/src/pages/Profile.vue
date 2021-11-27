<template v-if="isAuth">
  <div class="container">
    <div class="row">
      <div class="col-2">
        <div class="card card_user">
            <img v-if="!currentUser.avatar" class="card_user__image" src="../assets/image/user-icon.png" alt="Татьяна">
            <img v-if="currentUser.avatar" class="card_user__image" :src="currentUser.avatar" alt="Татьяна">
        </div>
        <input type="file" multiple>
      </div>
      <div class="card card_no-border col-md-8">
        <div class="card__title">
          {{currentUser.name}} {{currentUser.surname}} {{currentUser.patronymic}},
          {{currentUser.age}} {{currentUser.ageText}}
          <br>
          Email: {{currentUser.email}}
          <br>
          Телефон: {{currentUser.phone}}
        </div>s
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
      currentUser: state => state.auth.currentUser,
      isAuth: state => state.auth.isAuth
    })
  },
  methods: {
  },

}
</script>

<style scoped>
.card_user {
  -webkit-box-shadow: none;
  box-shadow: none;
  width: 120px;
  height: 120px;
}

.card_user__image {
  width: 100%;
  height: 100%;
}
</style>