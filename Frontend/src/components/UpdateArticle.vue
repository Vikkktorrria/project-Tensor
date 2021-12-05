<template>
  <h3 class="card__title">
    Изменить новость
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
        <div class="form__el-input">
          <textarea
              class="form__input form_card__textarea"
              rows="5"
              placeholder="Текс новости"
              v-model.trim="v$.text.$model"
          >
          </textarea>
          <small v-if="v$.text.required">Введите текст</small>
        </div>
      </div>
      <label
          class="card"
          for="input__file"
      >
        <div class="add-file">
          Изменить картинку
        </div>
        <input
            id="input__file"
            type="file"
            style="display: none"
            accept="image/jpeg,image/png"
            name="file"
            placeholder="Фото"
            @change="getFile"
        />
      </label>
      <div class="form__button form_card__button">
        <button class="btn">
          Редактировать новость
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
  name: "UpdateArticle",
  data() {
    return {
      v$: useVuelidate(),
      title: '',
      text: '',
      article_img: File,
    }
  },
  props: {
    article: {
      type:Array,
      required: true,
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
    getFile(e) {
      this.article_img = e.target.files[0]
    },
    async createNews(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        if (this.article_img) {
          try {
            let formData = new FormData();
            formData.append('file', this.article_img)
            const response = await axios.post(`http://127.0.0.1:5000/api/user/change/article/img/${this.article.id}`, formData, {
              headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
              'Content-Type': 'multipart/form-data'
            })
          } catch (error) {
            console.log(error)
          }
        }
        try {
          const response = await axios.put(`http://127.0.0.1:5000/api/user/change/article/${this.article.id}`, {
            title: this.title,
            text: this.text,
          }, {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
          })
        } catch (error) {
          console.log(error.request.response)
        } finally {
          this.$emit('create', this.title)
        }
      }
    },
    installArticle() {
      console.log(this.article)
      this.title = this.article.title
      this.text = this.article.text
    }
  },
  mounted() {
    this.installArticle()
  }
}
</script>

<style scoped>
.card__text {
  width: 500px;
}
textarea {
  resize: none;
  width: 500px;
}
.add-file {
  padding: 10px;
  border-radius: 5px;
  background-color: rgba(81, 148, 239, 0.6);
  border: 1px solid rgba(81, 148, 239, 0.9);
}
.form_card__input, .form__input {
  margin: 0;
}
.form__el-input {
  width: 100%;
}
</style>