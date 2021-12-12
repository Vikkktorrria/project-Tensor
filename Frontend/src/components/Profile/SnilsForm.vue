<template>
  <div
      :class="{
        'card card_no-border col-md-5': !currentUser.snils,
        'card card_no-border green col-md-5': currentUser.snils
      }"
  >
    <h3 class="card__title">
      СНИЛС
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
          <div class="form__el-text" v-if="!currentUser.snils">
            Номер:
          </div>
          <div class="form__el-input" v-if="!currentUser.snils">
            <input
                type="text"
                class="form__input form_card__input"
                placeholder="111222333 44"
                v-model.trim="v$.snils.$model"
            >
            <small v-if="v$.snils.minLength">Минимум 11 цифр</small>
          </div>
          <div class="form__el-input" v-if="currentUser.snils">
            <p>{{currentUser.snils}}</p>
          </div>
        </div>
        <div class="form__button form_card__button" v-if="!currentUser.snils">
          <button class="btn">
            Сохранить
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
import {mapActions, mapState} from "vuex";
const regexSnils = helpers.regex(/^(?!^0+$)[a-zA-Z0-9]{3,20}$/);
export default {
  name: "SnilsForm",
  data() {
    return {
      v$: useVuelidate(),
      snils: '',
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
      snils: {
        required,
        numeric,
        minLength: minLength(11)
      }
    }
  },
  methods: {
    ...mapActions({
      checkAuth: 'auth/checkAuth'
    }),
    async submitHandlerSnils(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          const response = await axios.post('http://127.0.0.1:5000/api/user/snils', {
            snils: this.snils,
          }, {
            headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
          })
          console.log(response)
          await this.checkAuth()
        } catch (error) {
          alert(error.request.response)
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
.green {
  background: #C7E0C5;
}
.green h3 {
  display: flex;
  justify-content: center;
}
.green>div, .green>div>form, .green>div>form>div {
  height: 100%;
  weight: 100%;
}
.green>div>form>div {
  padding-top: 20px;
  display: flex;
  justify-content: center;
  align-items: start;
  font-size: 28px;
}
</style>