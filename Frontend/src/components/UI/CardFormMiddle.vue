<template>
  <div class="card card_no-border col-md-5">
    <h3 class="card__title">
      {{ title }}
    </h3>
    <div class="card__text">
      <form class="form form_card" @submit.prevent="submitHandler">
        <div v-for="input in formInputs"
            class="form__el form_card__el"
            :class="{
              'form__el form_card__el error': input.error,
              'form__el form_card__el success': !input.error && input.dirty
            }"
        >
          <div class="form__el-text">
            {{input.text}}
          </div>
          <input
              type="text"
              class="form__input form_card__input"
              :placeholder="input.placeholder"
              v-model.trim="input.model"
          >
          <small v-if="input.regex.error">{{input.regex.message}}</small>
          <small v-if="input.required.error">{{input.required.message}}</small>
        </div>
        <div class="form__button form_card__button">
          <button class="btn">
            {{ buttonText }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CardFormMiddle",
  props: {
    title: {
      type: String,
      required: true
    },
    formInputs: {
      type: Array,
      required: true
    },
    buttonText: {
      type: String,
      required: true
    },
    submitHandler: {
      type: Function,
      required: true
    }
  },
}
</script>

<style scoped>

</style>