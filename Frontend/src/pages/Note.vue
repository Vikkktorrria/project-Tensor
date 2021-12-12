<template>
  <h1 class="h1-text">Запись</h1>
  <select-doctor
      v-if="!currentUser.isDoctor"
      @selected="selectedDoctor"
  ></select-doctor>
  <calendar
      v-if="currentDoctor || currentUser.isDoctor"
      :doctor="currentDoctor"
  >
  </calendar>
</template>

<script>
import SelectDoctor from "../components/Note/SelectDoctor";
import Calendar from "../components/Note/Calendar";
import {mapState} from "vuex";

let eventGuid = 0
let selInfo;
export default {
  name: "Note",
  data() {
    return {
      currentDoctor: '',
    }
  },
  methods: {
    selectedDoctor(doctor) {
      this.currentDoctor = doctor
    },
  },
  components: {
    SelectDoctor,
    Calendar
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
    })
  },
}
</script>

<style>
</style>