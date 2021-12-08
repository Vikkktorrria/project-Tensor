<template>
  <div v-if="!currentUser.isDoctor" class="container">
    <head-profile></head-profile>
  </div>
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
  <div v-if="!currentUser.isDoctor" class="container">
    <div class="row">
      <anamnesis-form
          :current-user="currentUser"
      ></anamnesis-form>
    </div>
  </div>
  <div v-if="currentUser.isDoctor" class="container">
    <div class="row">
      <div class="card card_no-border col-md-8">
        <div class="card__title">
          {{currentUser.surname}} {{currentUser.name}} {{currentUser.patronymic}},
          {{currentUser.age}} {{currentUser.ageText}}
          <br>
          Email: {{currentUser.email}}
          <br>
          Телефон: {{currentUser.phone}}
          <br>
          Квалификация: {{this.doctorData.qualification}}
          <br>
          Опыт работы: {{this.doctorData.experience}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PassportForm from "../components/PassportForm";
import SnilsForm from "../components/SnilsForm";
import AnamnesisForm from "../components/AnamnesisForm";
import HeadProfile from "../components/HeadProfile";
import {mapState} from "vuex";
import axios from "axios";
export default {
  name: "Profile",
  components: {
    HeadProfile,
    PassportForm,
    SnilsForm,
    AnamnesisForm
  },
  data() {
    return {
      doctorData: []
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
      isAuth: state => state.auth.isAuth
    }),
  },
  methods: {

    async fetchDoctor() {
      if (this.currentUser.isDoctor) {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/user/doctor/info', {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
          })
          this.doctorData = response.data
          console.log(response.data)
        } catch (error) {
          console.log(error)
        } finally {
        }
      }
    }
  },
  mounted() {
    this.fetchDoctor()
  }
}
</script>

<style scoped>
</style>