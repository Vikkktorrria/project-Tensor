<template>
  <h3 class="card__title">
    Вы уверены, что хотите создать запись?
  </h3>
  <div class="card__text">
    <form class="form form_card" @submit.prevent="sendText">
      <div class="form__button form_card__button">
        <button class="btn"
                @click="sendText">
          Да
        </button>
        <button class="btn" @click="sendFalse">
          Нет
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "CreateNote",
  props: {
    doctor: {
      type: Array
    }
  },
  methods: {
    sendFalse() {
      this.$emit('create', false)
    },
    sendText() {
      this.$emit('create', this.doctor)
    }
  }
}
</script>

<style scoped>
.btn {
  margin: 10px;
  font-size: 20px;
}
</style>