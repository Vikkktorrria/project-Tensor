<template>
  <div class="card card_no-border col-md-12">
    <h3 class="card__title">
      Пароль
    </h3>
    <div class="card__text">
      <form class="form form_card"   @submit.prevent="submitHandlerPassword">
        <div
            class="form__el form_card__el"
            :class="{
          'form__el form_card__el error': v$.passwordOld.$error,
          'form__el form_card__el success': !v$.passwordOld.$error && v$.passwordOld.$dirty
        }"
        >
          <div class="form__el-text">
            Старый пароль:
          </div>
          <div class="form__el-input">
            <input
                type="password"
                class="form__input form_card__input form_card__input-settings"
                placeholder="******"
                v-model.trim="v$.passwordOld.$model"
            >
            <small v-if="v$.passwordOld.minLength">Поле пароль некорректно (минимум 6 символов)</small>
          </div>
        </div>
        <div
            class="form__el form_card__el"
            :class="{
          'form__el form_card__el error': v$.password.$error,
          'form__el form_card__el success': !v$.password.$error && v$.password.$dirty
        }"
        >
          <div class="form__el-text">
            Новый пароль:
          </div>
          <div class="form__el-input">
            <input
                type="password"
                class="form__input form_card__input form_card__input-settings"
                placeholder="******"
                v-model.trim="v$.password.$model"
            >
            <small v-if="v$.password.minLength">Поле пароль некорректно (минимум 6 символов)</small>
          </div>
        </div>
        <div
            class="form__el form_card__el"
            :class="{
          'form__el form_card__el error': v$.repeatPassword.$error || v$.password.$model !== v$.repeatPassword.$model,
          'form__el form_card__el success': (!v$.repeatPassword.$error && v$.repeatPassword.$dirty)
        }"
        >
          <div class="form__el-text">
            Повторите:
          </div>
          <div class="form__el-input">
            <input
                type="password"
                class="form__input form_card__input form_card__input-settings"
                placeholder="******"
                v-model.trim="v$.repeatPassword.$model"
            >
            <small v-if="v$.repeatPassword.$model === ''">Поле повторный пароль не может быть пустым</small>
            <small v-if="v$.password.$model !== v$.repeatPassword.$model && v$.repeatPassword.$model !== ''">Пароль не совпадает</small>
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
import {minLength, required} from "@vuelidate/validators";
import axios from "axios";

export default {
  name: "ChangePasswordForm",
  data() {
    return {
      v$: useVuelidate(),
      password: '',
      passwordOld: '',
      repeatPassword: '',
    }
  },
  validations() {
    return {
      passwordOld: {
        required,
        minLength: minLength(6)
      },
      password: {
        required,
        minLength: minLength(6)
      },
      repeatPassword: {
        required,
        minLength: minLength(6)
      },
    }
  },
  methods: {
    async submitHandlerPassword(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          const response = await axios.put('http://127.0.0.1:5000/api/user/change/password', {
            password: this.password,
            passwordOld: this.passwordOld,
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