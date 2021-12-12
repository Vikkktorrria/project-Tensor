<template>
  <h3 class="card__title">
    Выберете врача
  </h3>
  <div class="card__text">
    <form class="form form_card">
      <div
          class="form__el form_card__el"
      >
        <div class="form__el-text">
          Врач:
        </div>
        <div class="form__el-input">
          <select
              v-model="idDoctor"
              @change="setIdDoctor(idDoctor)"
              class="form__input form_card__input"
          >
            <option disabled value="">Выберите...</option>
            <option
                v-for="doctor in doctors"
                :key="doctor.id"
                :value="doctor.id"
            >{{ doctor.qualification }}: {{ doctor.fullName.surname }} {{ doctor.fullName.name }}</option>
          </select>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SelectDoctor",
  data() {
    return {
      idDoctor: '',
      doctors: [],
    }
  },
  methods: {
    async fetchDoctors(e) {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/doctors/all', {
          headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
        })
        this.doctors = response.data
      } catch (error) {
        alert(error.request.response)
      } finally {

      }
    },
    setIdDoctor(id) {
      this.$emit('selected', this.doctors.find(doctor => doctor.id === this.idDoctor))
    }
  },
  mounted() {
    this.fetchDoctors()
  }
}
</script>

<style scoped>
.form__el-text {
  font-size: 20px;
  width: 100px;
}
.card__title, .form__el {
  color: #35538D;
  display: flex;
  justify-content: start;
}
</style>