<template>
  <div class="card card_no-border col-md-5">
    <h3 class="card__title">
      Снилс
    </h3>
    <div class="card__text">
      <form class="form form_card" @submit.prevent="submitHandlerSnils">
        <div
            class="form__el form_card__el"
            :class="{
                  'form__el form_card__el error': v$.snils.$error,
                  'form__el form_card__el success': !v$.snils.$error && v$.snils.$dirty
                }"
        >
          <div class="form__el-text">
            Номер:
          </div>
          <div class="form__el-input">
            <input
                type="text"
                class="form__input form_card__input"
                placeholder="111-222-333333"
                v-model.trim="v$.snils.$model"
            >
            <small v-if="v$.snils.minLength">Минимум 12 цифр</small>
          </div>
        </div>
        <div class="form__button form_card__button">
          <button class="btn">
            Изменить
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {numeric, required, email, minLength, helpers} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";
import axios from "axios";
const regexSnils = helpers.regex(/^(?!^0+$)[a-zA-Z0-9]{3,20}$/);
export default {
  name: "SnilsForm",
  data() {
    return {
      v$: useVuelidate(),
      snils: '',
    }
  },
  validations() {
    return {
      snils: {
        required,
        numeric,
        minLength: minLength(12)
      }
    }
  },
  methods: {
    async submitHandlerSnils(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          const response = await axios.post('http://127.0.0.1:5000/api/user/snilss', {
            snils: this.snils,
          }, {
            headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
          })
          console.log(response)
        } catch (error) {
          console.log(error.response)
          alert(error.response.data)
        } finally {

        }
      }
    },
  }
}
</script>

<style scoped>
.form__el-input {position: relative}
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