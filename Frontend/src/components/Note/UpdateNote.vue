<template>
  <h3 class="card__title">
    {{note.patient.surname}} {{note.patient.name}} {{note.patient.patronymic}}
  </h3>
  <p class="card-p" >Анамнез: {{note.patient.anamnesis}}</p>
  <div class="card__text">
    <form class="form form_card" @submit.prevent="createNote">
      <div class="form__row">
        <div
            class="form__el form_card__el"
            :class="{
                  'form__el form_card__el error': v$.diagnosis.$error,
                  'form__el form_card__el success': !v$.diagnosis.$error && v$.diagnosis.$dirty
                }"
        >
          <div class="form__el-input">
            <p class="text-input">Диагноз</p>
            <textarea
                class="form__input form_card__textarea"
                rows="5"
                placeholder="Диагноз"
                v-model.trim="v$.diagnosis.$model"
            >
          </textarea>
            <small v-if="v$.diagnosis.required">Введите текст</small>
          </div>
        </div>
        <hr class="vertical" />
        <div
            class="form__el form_card__el"
            :class="{
                'form__el form_card__el error': v$.recipe.$error,
                'form__el form_card__el success': !v$.recipe.$error && v$.recipe.$dirty
              }"
        >
          <div class="form__el-input">
            <p class="text-input">Рецепт</p>
            <textarea
                class="form__input form_card__textarea"
                rows="5"
                placeholder="Рецепт"
                v-model.trim="v$.recipe.$model"
            >
          </textarea>
            <small v-if="v$.recipe.required">Введите текст</small>
          </div>
        </div>
      </div>
      <div class="form__button form_card__button">
        <button class="btn">
          Сохранить
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
  name: "UpdateNote",
  data() {
    return {
      v$: useVuelidate(),
      diagnosis: '',
      recipe: '',
    }
  },
  props: {
    note: {
      type:Array,
      required: true,
    }
  },
  validations() {
    return {
      diagnosis: {
        required
      },
      recipe: {
        required
      },
    }
  },
  methods: {
    async createNote(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        console.log('error')
      } else {
        try {
          const response = await axios.put(`http://127.0.0.1:5000/api/user/doctor/change/note/${this.note.id}`, {
            diagnosis: this.diagnosis,
            recipe: this.recipe,
          }, {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
          })
        } catch (error) {
          alert(error.request.response)
        } finally {
          this.$emit('create', this.title)
        }
      }
    },
    async installArticle() {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/user/doctor/note/${this.note.id}`, {
          headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
        })
        this.diagnosis = response.data.diagnosis
        this.recipe = response.data.recipe
      } catch (error) {
        alert(error.request.response)
      }
    }
  },
  mounted() {
    this.installArticle()
  }
}
</script>

<style scoped>
.card__text {
  width: 1000px;
}
textarea {
  resize: none;
  width: 400px;
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
.text-input {
  padding-left: 20px;
  font-size: 24px;
}
.card-p {
  font-size: 18px;
}
.form__row {
  display: flex;
  justify-content: space-between;
}
.vertical {
  border: 0;
  margin: 0;
  border-left: 1px solid rgba(121, 139, 164, 0.2);
  height: 200px;
  float: left;
}
</style>