<template>
  <div class="container">
    <head-profile></head-profile>
  </div>
  <profile-patient></profile-patient>
</template>

<script>
import HeadProfile from "../components/Profile/HeadProfile";
import ProfilePatient from "../components/Profile/ProfilePatient";
import {mapState} from "vuex";
export default {
  name: "Profile",
  components: {
    HeadProfile,
    ProfilePatient
  }
}
</script>

<style scoped>
</style>