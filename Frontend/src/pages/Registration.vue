<template>
  <h1 class="h1-text">Регистрация</h1>
  <div class="content__container">
    <form class="form" @submit.prevent="submitHandler">
      <div
          class="form__el"
          :class="{
          'form__el error': v$.name.$error,
          'form__el success': !v$.name.$error && v$.name.$dirty
        }"
      >
        <input
            type="text"
            class="form__input"
            placeholder="Имя"
            v-model.trim="v$.name.$model"
        >
        <small v-if="v$.name.minLength">Поле имя не может быть пустым (минимум 3 символа)</small>
      </div>
      <div
          class="form__el"
          :class="{
          'form__el error': v$.lastName.$error,
          'form__el success': !v$.lastName.$error && v$.lastName.$dirty
        }"
      >
        <input
            type="text"
            class="form__input"
            placeholder="Фамилия"
            v-model.trim="v$.lastName.$model"
        >
        <small v-if="v$.name.minLength">Поле фамилия не может быть пустым (минимум 4 символа)</small>
      </div>
      <div class="form__el">
        <input
            type="text"
            class="form__input"
            placeholder="Отчество"
        >
      </div>
      <div
          class="form__el"
          :class="{
          'form__el error': v$.email.$error,
          'form__el success': !v$.email.$error && v$.email.$dirty
        }"
      >
        <input
            type="text"
            class="form__input"
            placeholder="Почта"
            v-model.trim="v$.email.$model"
        >
        <small v-if="v$.email.$model === ''">Поле почта не может быть пустым</small>
        <small v-if="v$.email.email.$invalid">Поле почта не корректно</small>
      </div>
      <div
          class="form__el"
          :class="{
          'form__el error': v$.phone.$error,
          'form__el success': !v$.phone.$error && v$.phone.$dirty
        }"
      >
        <input
            type="text"
            class="form__input"
            placeholder="Телефон"
            v-model.trim="v$.phone.$model"
        >
        <small v-if="v$.phone.minLength || v$.phone.numeric">Поле телефон не корректно</small>
      </div>
      <div
          class="form__el"
          :class="{
          'form__el error': v$.password.$error,
          'form__el success': !v$.password.$error && v$.password.$dirty
        }"
      >
        <input
            type="password"
            class="form__input"
            placeholder="Пароль"
            v-model.trim="v$.password.$model"
        >
        <small v-if="v$.password.minLength">Поле пароль не корректно (минимум 6 символов)</small>
      </div>
      <div
          class="form__el"
          :class="{
          'form__el error': v$.repeatPassword.$error || v$.password.$model !== v$.repeatPassword.$model,
          'form__el success': (!v$.repeatPassword.$error && v$.repeatPassword.$dirty)
        }"
      >
        <input
            type="password"
            class="form__input"
            placeholder="Повторите пароль"
            v-model.trim="v$.repeatPassword.$model"
        >
        <small v-if="v$.repeatPassword.$model === ''">Поле повторный пароль не может быть пустым</small>
        <small v-if="v$.password.$model !== v$.repeatPassword.$model && v$.repeatPassword.$model !== ''">Пароль не
          совпадает</small>
      </div>
      <div class="form__el form__el_checkbox">
        <input
            type="checkbox"
            id="notification"
            v-model.trim="v$.notification.$model"
        >
        <p class="form__text-p">Сообщать об изменениях по почте</p>
      </div>
      <div
          class="form__el form__el_checkbox"
          :class="{
          'form__el form__el_checkbox error': !v$.consent.$model,
          'form__el form__el_checkbox success': v$.consent.$model
        }"
      >
        <input
            type="checkbox"
            id="consent"
            v-model.trim="v$.consent.$model"
        >
        <p class="form__text-p">
          Подтверждаю согласие
          <span class="form__text-span">с политикой обработки персональных данных</span>
          <small v-if="!v$.consent.$model">Подтвердите согласие</small>
        </p>
      </div>
      <div class="form__button">
        <button class="btn">
          {{ buttonText }}
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import {numeric, required, email, minLength} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";
import axios from "axios";

export default {
  name: "Registration",
  data() {
    return {
      v$: useVuelidate(),
      name: '',
      lastName: '',
      patronymic: '',
      email: '',
      phone: '',
      password: '',
      repeatPassword: '',
      notification: false,
      consent: true,
      buttonText: 'Зарегестрироваться'
    }
  },
  validations() {
    return {
      name: {
        required,
        minLength: minLength(3)
      },
      lastName: {
        required,
        minLength: minLength(4)
      },
      patronymic: {},
      email: {
        required,
        email
      },
      phone: {
        required,
        numeric,
        minLength: minLength(10)
      },
      password: {
        required,
        minLength: minLength(6)
      },
      repeatPassword: {
        required,
        minLength: minLength(6)
      },
      notification: {},
      consent: {
        required,
      }
    }
  },
  methods: {
    async submitHandler(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          const response = await axios.post('http://127.0.0.1:5000/api/auth/registration', {
            headers: {'Content-type': 'application/json'},
            name: this.v$.name,
            lastName: this.v$.lastName,
            patronymic: this.v$.patronymic,
            phone: this.v$.phone,
            email: this.v$.email,
            password: this.v$.password,
            birthday: new Date(2011, 0, 1)
            // notification: this.v$.notification,
          })
          console.log(response)
        } catch (error) {
          alert(error)
        } finally {

        }
      }
    },
    updateInput(e) {
      this.$emit('update:value', e.target.value);
    }
  }
}
</script>

<style scoped>

</style>