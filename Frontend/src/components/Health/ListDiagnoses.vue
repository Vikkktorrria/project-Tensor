<template>
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
          <p>{{diagnosis.doctor.qualification}}: {{diagnosis.doctor.surname}} {{diagnosis.doctor.name}} {{diagnosis.doctor.patronymic}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ListDiagnoses",
  props: {
    diagnoses: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style scoped>
</style>