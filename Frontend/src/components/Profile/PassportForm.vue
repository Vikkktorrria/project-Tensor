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
          <div class="form__el-input" v-if="!currentUser.passport.series">
            <input
                type="text"
                class="form__input form_card__input"
                placeholder="1111"
                v-model.trim="v$.passportSeries.$model"
            >
            <small v-if="v$.passportSeries.minLength">Минимум 4 цифры</small>
          </div>
          <div class="form__el-input" v-if="currentUser.passport.series">
            <p>{{currentUser.passport.series}}</p>
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
          <div class="form__el-input" v-if="!currentUser.passport.number">
            <input
                type="text"
                class="form__input form_card__input"
                placeholder="222222"
                v-model.trim="v$.passportId.$model"
            >
            <small v-if="v$.passportId.minLength">Минимум 6 цифр</small>
          </div>
          <div class="form__el-input" v-if="currentUser.passport.number">
            <p>{{currentUser.passport.number}}</p>
          </div>
        </div>
        <div class="form__button form_card__button" v-if="!currentUser.passport.number">
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
import {mapActions, mapState} from "vuex";
export default {
  name: "PassportForm",
  data() {
    return {
      v$: useVuelidate(),
      passportSeries: '',
      passportId: '',
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
    ...mapActions({
      checkAuth: 'auth/checkAuth'
    }),
    async submitHandlerPassport(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          const response = await axios.post('http://127.0.0.1:5000/api/user/passport', {
            passportSeries: this.passportSeries,
            passportNumber: this.passportId
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