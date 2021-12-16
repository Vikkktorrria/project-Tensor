<template>
  <div v-if="(currentUser.snils && currentUser.anamnesis && currentUser.passport.number) || (currentUser.isDoctor)">
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
  </div>
  <div v-else>
    <h1 class="h1-text">Запись</h1>
    <h3 class="error__title">
      Сначала заполните профиль на 100%
    </h3>
  </div>
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
.error__title {
  color: #35538D;
  font-size: 24px;
  display: flex;
  justify-content: center;
}
</style>