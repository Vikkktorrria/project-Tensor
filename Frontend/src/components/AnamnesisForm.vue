<template>
  <div class="card card_no-border col-md-11">
    <h3 class="card__title">
      Анамнез
    </h3>
    <div class="card__text">
      <form class="form form_card" @submit.prevent="submitHandlerAnamnesis">
        <div
            class="form__el form_card__el"
            :class="{
                  'form__el form_card__el error': v$.anamnesis.$error,
                  'form__el form_card__el success': !v$.anamnesis.$error && v$.anamnesis.$dirty
                }"
        >
          <textarea
              class="form__input form_card__textarea"
              rows="10"
              v-model.trim="v$.anamnesis.$model"
              v-model="currentUser.anamnesis"
          >
          </textarea>
          <small v-if="v$.anamnesis.required">Введите данные</small>
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
import {numeric, required, email, minLength, maxLength} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";
import axios from "axios";
import {mapActions, mapState} from "vuex";
export default {
  name: "AnamnesisForm",
  data() {
    return {
      v$: useVuelidate(),
      anamnesis: '',
    }
  },
  props: {
    currentUser: {
      type: Object,
      required: true
    }
  },
  validations() {
    return {
      anamnesis: {
        required,
      }
    }
  },
  methods: {
    ...mapActions({
      checkAuth: 'auth/checkAuth'
    }),
    async submitHandlerAnamnesis(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          const response = await axios.post('http://127.0.0.1:5000/api/user/anamnesis', {
            anamnesis: this.anamnesis,
          }, {
            headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
          })
          await this.checkAuth()
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
.form_card__textarea {width: 100%}
textarea {
  resize: none;
}
</style>