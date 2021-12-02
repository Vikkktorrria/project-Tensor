<template>
  <h3 class="card__title">
    Создание новости
  </h3>
  <div class="card__text">
    <form class="form form_card" @submit.prevent="createNews">
      <div
          class="form__el form_card__el"
          :class="{
                  'form__el form_card__el error': v$.title.$error,
                  'form__el form_card__el success': !v$.title.$error && v$.title.$dirty
                }"
      >
        <div class="form__el-text">
          Заголовок:
        </div>
        <div class="form__el-input">
          <input
              type="text"
              class="form__input form_card__input form_card__input-settings"
              placeholder="Заголовок"
              v-model.trim="v$.title.$model"
          >
          <small v-if="v$.title.required">Введите заголовок</small>
        </div>
      </div>
      <div
          class="form__el form_card__el"
          :class="{
                  'form__el form_card__el error': v$.text.$error,
                  'form__el form_card__el success': !v$.text.$error && v$.text.$dirty
                }"
      >
        <div class="form__el-text">
          Текс новости:
        </div>
        <div class="form__el-input">
          <textarea
              class="form__input form_card__textarea"
              rows="10"
              v-model.trim="v$.text.$model"
          >
          </textarea>
          <small v-if="v$.text.required">Введите текст</small>
        </div>
      </div>
      <div class="form__button form_card__button">
        <button class="btn">
          Добавить новость
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import {numeric, required, minLength} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";
import axios from "axios";

export default {
  name: "CreateArticle",
  data() {
    return {
      v$: useVuelidate(),
      title: '',
      text: '',
      article_img: ''
    }
  },
  validations() {
    return {
      title: {
        required
      },
      text: {
        required
      },
    }
  },
  methods: {
    async createNews(e) {
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/user/article', {
          title: this.title,
          text: this.text,
          article_img: this.article_img
        }, {
          headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
        })
      } catch (error) {
        alert(error.request.response)
      } finally {
        this.$emit('create', this.title)
      }
    },
  },
}
</script>

<style scoped>
.card__title, .form__el {
  display: flex;
  justify-content: center;
}
</style>