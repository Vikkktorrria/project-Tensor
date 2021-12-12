<template>
  <div class="card card_no-border col-md-12">
    <h3 class="card__title">
      E-mail
    </h3>
    <div class="card__text">
      <form class="form form_card"  @submit.prevent="submitHandlerEmail">
        <div
            class="form__el form_card__el"
            :class="{
          'form__el form_card__el error': v$.email.$error,
          'form__el form_card__el success': !v$.email.$error && v$.email.$dirty
        }"
        >
          <div class="form__el-text">
            Введите почту:
          </div>
          <div class="form__el-input">
            <input
                type="text"
                class="form__input form_card__input form_card__input-settings"
                placeholder="name@mail.ru"
                v-model.trim="v$.email.$model"
            >
            <small v-if="v$.email.$model === ''">Поле почта не может быть пустым</small>
            <small v-if="v$.email.email.$invalid">Поле почта некорректно</small>
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
import useVuelidate from "@vuelidate/core";
import {email, required} from "@vuelidate/validators";
import axios from "axios";

export default {
  name: "ChangeEmailForm",
  data() {
    return {
      v$: useVuelidate(),
      email: '',
    }
  },
  validations() {
    return {
      email: {
        required,
        email
      },
    }
  },
  methods: {
    async submitHandlerEmail(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          const response = await axios.put('http://127.0.0.1:5000/api/user/change/email', {
            email: this.email
          }, {
            headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
          })
          console.log(response)
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
.form__input {width: 95%;}
.form__el-input {
  width: 100%;
  position: relative
}
small {
  left: 10px;
}
</style>