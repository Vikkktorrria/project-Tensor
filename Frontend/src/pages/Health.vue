<template>
  <h1 class="h1-text">Диагнозы</h1>
  <div class="container container_only-row">
    <div
        class="row"
        v-for="diagnosis in diagnoses"
        :key="diagnosis.id"
    >
      <div
          class="card card_no-border col-md-8"
          href="#"
      >
        <div class="card__text">
          Диагноз: {{diagnosis.diagnosis}}
        </div>
        <div class="card__text">
          Рецепт: {{diagnosis.recipe}}
        </div>
        <div class="card__footer">
          <div class="card__date">
            {{diagnosis.dateAdded}}
          </div>
          <div class="card__name-doctor">
            {{diagnosis.doctor.name}} {{diagnosis.doctor.surname}} {{diagnosis.doctor.patronymic}}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Health",
  data() {
    return {
      diagnoses: [
        {
          id: 1,
          diagnosis: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto assumenda consequatur obcaecati distinctio sint minima porro saepe nisi dolor fugit tempore dolores magni enim, recusandae neque voluptas et sunt veniam?',
          recipe: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto assumenda consequatur obcaecati distinctio sint minima porro saepe nisi dolor fugit tempore dolores magni enim, recusandae neque voluptas et sunt veniam?',
          dateAdded: '2020-12-31',
          doctor: {
            name: 'Иван',
            surname: 'Иванов',
            patronymic: 'Иванович',
          }
        },
        {
          id: 2,
          diagnosis: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto assumenda consequatur obcaecati distinctio sint minima porro saepe nisi dolor fugit tempore dolores magni enim, recusandae neque voluptas et sunt veniam?',
          recipe: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto assumenda consequatur obcaecati distinctio sint minima porro saepe nisi dolor fugit tempore dolores magni enim, recusandae neque voluptas et sunt veniam?',
          dateAdded: '2020-12-31',
          doctor: {
            name: 'Иван',
            surname: 'Иванов',
            patronymic: 'Иванович',
          }
        },
      ],
    }
  },
  methods: {
    async fetchNews(e) {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/user/diagnoses', {
          headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
        })
        console.log(response)
        this.diagnoses = [...this.diagnoses, ...response.data]
      } catch (error) {
        alert(error.request.response)
      } finally {

      }
    },
  },
  mounted() {
    this.fetchNews()
  }
}
</script>

<style scoped>
</style>