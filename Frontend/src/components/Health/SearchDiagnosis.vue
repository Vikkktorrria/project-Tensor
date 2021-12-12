<template>
  <DatePicker v-model="date" />
  <div class="form__button form_card__button">
    <button class="btn" @click="setDate">
      Поиск
    </button>
  </div>
</template>

<script>
import { DatePicker } from 'v-calendar';
export default {
  name: "SearchDiagnosis",
  components: {
    DatePicker
  },
  data() {
    return {
      date: '',
    }
  },
  methods: {
    onContext(ctx) {
      this.context = ctx
    },
    setDate() {
      this.$emit('filter', this.date)
    }
  }
}
</script>

<style scoped>
.form__button {
  margin-top: 10px;
}
</style>