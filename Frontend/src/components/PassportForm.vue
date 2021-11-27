<template>
  <div class="card card_no-border col-md-5">
    <h3 class="card__title">
      Паспортные данные
    </h3>
    <div class="card__text">
      <form class="form form_card" @submit.prevent="submitHandlerPassport">
        <div
            class="form__el form_card__el"
            :class="{
                  'form__el form_card__el error': v$.passportSeries.$error,
                  'form__el form_card__el success': !v$.passportSeries.$error && v$.passportSeries.$dirty
                }"
        >
          <div class="form__el-text">
            Серия:
          </div>
          <div class="form__el-input">
            <input
                type="text"
                class="form__input form_card__input"
                placeholder="1111"
                v-model.trim="v$.passportSeries.$model"
            >
            <small v-if="v$.passportSeries.minLength">Минимум 4 цифры</small>
          </div>
        </div>
        <div
            class="form__el form_card__el"
            :class="{
                  'form__el form_card__el error': v$.passportId.$error,
                  'form__el form_card__el success': !v$.passportId.$error && v$.passportId.$dirty
                }"
        >
          <div class="form__el-text">
            Номер:
          </div>
          <div class="form__el-input">
            <input
                type="text"
                class="form__input form_card__input"
                placeholder="222222"
                v-model.trim="v$.passportId.$model"
            >
            <small v-if="v$.passportId.minLength">Минимум 6 цифр</small>
          </div>
        </div>
        <div class="form__button form_card__button">
          <button class="btn">
            Сохранить
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {numeric, required, minLength} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";
import axios from "axios";
export default {
  name: "PassportForm",
  data() {
    return {
      v$: useVuelidate(),
      passportSeries: '',
      passportId: '',
    }
  },
  validations() {
    return {
      passportSeries: {
        required,
        numeric,
        minLength: minLength(4)
      },
      passportId: {
        required,
        numeric,
        minLength: minLength(6)
      }
    }
  },
  methods: {
    async submitHandlerPassport(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          console.log('yes')
          const response = await axios.post('http://127.0.0.1:5000/api/user/passport', {
            headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
            passportSeries: passportSeries,
            passportNumder: passportId
          })
          console.log(response)
        } catch (error) {
          console.log(error)
        } finally {

        }
      }
    },
  }
}
</script>

<style scoped>
.form__el-input {
  position: relative
}
small {
  left: 10px;
}
.form_card__input {
  width: 90%;
}
.card {
  justify-content: space-between;
}
</style>