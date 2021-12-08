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
            {{diagnosis.date_of_visit}}
          </div>
          <div class="card__name-doctor">
            {{diagnosis.doctor.surname}} {{diagnosis.doctor.name}} {{diagnosis.doctor.patronymic}}
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
      diagnoses: [],
    }
  },
  methods: {
    async fetchNews(e) {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/user/diagnoses', {
          headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
        })
        let diagnoses = response.data
        diagnoses.forEach((el) => { el.date_of_visit = el.date_of_visit.split('T')[0] })
        this.diagnoses = [...this.diagnoses, ...diagnoses]
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