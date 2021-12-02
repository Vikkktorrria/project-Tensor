<template v-if="!isAuth">
  <h1 class="h1-text">Вход</h1>
  <div class="content__container">
    <form class="form" @submit.prevent="submitHandler">
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
        <small v-if="v$.email.email.$invalid">Поле почта некорректно</small>
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
        <small v-if="v$.password.minLength">Поле пароль некорректно (минимум 6 символов)</small>
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
import {numeric, required, email, minLength, helpers} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";
import axios from "axios";
import {mapMutations, mapState} from 'vuex';
export default {
  name: "Registration",
  data() {
    return {
      v$: useVuelidate(),
      email: '',
      password: '',
      buttonText: 'Войти'
    }
  },
  validations() {
    return {
      email: {
        required,
        email
      },
      password: {
        required,
        minLength: minLength(6)
      }
    }
  },
  methods: {
    ...mapMutations({
      setAuth: 'auth/setAuth',
      setUser: 'auth/setUser'
    }),

    async submitHandler(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          const username = this.v$.email.$model
          const password = this.v$.password.$model
          const token = Buffer.from(`${username}:${password}`, 'utf8').toString('base64')
          const response = await axios.get('http://127.0.0.1:5000/api/auth/auth', {
            headers: {'Authorization': `Basic ${token}`}
          })
          localStorage.setItem('token', response.data.token)
          this.setUser(response.data.user)
          this.setAuth(true)
          await  this.$router.push({ name: 'notification' });
        } catch (error) {
          alert(error.response)
        } finally {

        }
      }
    },
    updateInput(e) {
      this.$emit('update:value', e.target.value);
    }
  },
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth
    }),
  }
}
</script>

<style scoped>
</style>