<template>
  <div class="card card_no-border col-md-12">
    <h3 class="card__title">
      Уведомления
    </h3>
    <div class="card__text">
      <form class="form form_card" @submit.prevent="submitHandlerNotification">
        <div
            class="form__el form_card__el form__el_checkbox"
            :class="{
                  'form__el form_card__el form__el_checkbox error': !v$.notification.$model,
                  'form__el form_card__el form__el_checkbox success': v$.notification.$model
                }"
        >
          <input
              type="checkbox"
              id="consent"
              v-model.trim="v$.notification.$model"
          >
          <p class="form__text-p">
            Отправлять уведомления на почту
            <small v-if="!v$.notification.$model">Подтвердите согласие</small>
          </p>
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
import {required} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";
import axios from "axios";
export default {
  name: "NotificationForm",
  data() {
    return {
      v$: useVuelidate(),
      notification: true
    }
  },
  validations() {
    return {
      notification: {
        required
      },
    }
  },
  methods: {
    async submitHandlerNotification(e) {
      this.v$.$touch()
      if (!this.v$.notification.$model) {
        console.log('error')
      } else {
        try {
          const response = await axios.put('http://127.0.0.1:5000/api/user/change/notification', {
            notification: this.notification
          }, {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
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

</style>