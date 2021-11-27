<template v-if="isAuth">
  <div class="container">
<!--    <swiper></swiper>-->
    <div class="row">
      <a
          @click="$router.push('/profile')"
          class="card col-md-4"
      >
        <h3 class="card__title">
          Мой профиль
        </h3>
        <div class="card__text">
          Профиль заполнен на 67%
        </div>
      </a>
      <a
          @click="$router.push('/note')"
          class="card col-md-4"
      >
        <h3 class="card__title">
          Мои записи
        </h3>
        <div class="card__text">
          Ближайшая запись 22/10/2021
        </div>
      </a>
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";
export default {
  name: "Notification",
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth
    })
  },
}
</script>

<style scoped>

</style>