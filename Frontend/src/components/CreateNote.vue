<template>
  <h3 class="card__title">
    Создание записи
  </h3>
  <div class="card__text">
    <form class="form form_card" @submit.prevent="sendText">
      <div
          class="form__el form_card__el"
          :class="{
                  'form__el form_card__el error': v$.idDoctor.$error,
                  'form__el form_card__el success': !v$.idDoctor.$error && v$.idDoctor.$dirty
                }"
      >
        <div class="form__el-text">
          Врач:
        </div>
        <div class="form__el-input">
          <select
              v-model="v$.idDoctor.$model"
              class="form__input form_card__input"
          >
            <option disabled value="">Выберите...</option>
            <option
                v-for="doctor in doctors"
                :key="doctor.id"
                :value="doctor.id"
            >{{ doctor.fullName.surname }} {{ doctor.fullName.name }}</option>
          </select>
          <small v-if="!v$.idDoctor.required">Выберите врача</small>
        </div>
      </div>
      <div class="form__button form_card__button">
        <button class="btn"
                @click="sendText">
          Сохранить
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import {numeric, required, minLength} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";
import axios from "axios";
import toggleMixin from "../mixins/toggleMixin";

export default {
  name: "CreateNote",
  data() {
    return {
      v$: useVuelidate(),
      idDoctor: '',
      doctors: [],
      doctor: '',
    }
  },
  validations() {
    return {
      idDoctor: {
        required,
      }
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
    sendText() {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        this.doctors.forEach((el) => {
          if (el.id === this.idDoctor) {
            this.doctor = el
          }
        })
        this.$emit('create', this.doctor)
      }
    }
  },
  mixins: [toggleMixin],
  mounted() {
    this.fetchDoctors()
  }
}
</script>

<style scoped>
.card__title, .form__el {
  display: flex;
  justify-content: center;
}
</style>