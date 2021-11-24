<template>
  <div class="container">
    <div class="card-slider">
      <div class="swiper">
        <div class="swiper-wrapper">
          <div class="swiper-slide">
            <div class="swiper__slide-image">
              <a href="news.html"><img src="../assets/image/slide_1.png" alt=""></a>
            </div>
          </div>
          <div class="swiper-slide">
            <div class="swiper__slide-image">
              <a href="news.html"><img src="../assets/image/slide_2.jpg" alt=""></a>
            </div>
          </div>
          <div class="swiper-slide">
            <div class="swiper__slide-image">
              <a href="news.html"><img src="../assets/image/slide_3.jpg" alt=""></a>
            </div>
          </div>
        </div>
      </div>
      <div class="swiper-button-prev"></div>
      <div class="swiper-button-next"></div>
      <div class="swiper-pagination"></div>
    </div>
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
export default {
  name: "Notification"
}
</script>

<style scoped>

</style>