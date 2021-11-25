<template>
  <swiper
      :slides-per-view="3"
      :space-between="50"
      @swiper="onSwiper"
      @slideChange="onSlideChange"
  >
    <swiper-slide>Slide 1</swiper-slide>
    <swiper-slide>Slide 2</swiper-slide>
    <swiper-slide>Slide 3</swiper-slide>
    ...
  </swiper>
<!--  <div class="card-slider">-->
<!--    <div class="swiper">-->
<!--      <div class="swiper-wrapper">-->
<!--        <div class="swiper-slide">-->
<!--          <div class="swiper__slide-image">-->
<!--            <a href="news.html"><img src="../assets/image/slide_1.png" alt=""></a>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div class="swiper-slide">-->
<!--          <div class="swiper__slide-image">-->
<!--            <a href="news.html"><img src="../assets/image/slide_2.jpg" alt=""></a>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div class="swiper-slide">-->
<!--          <div class="swiper__slide-image">-->
<!--            <a href="news.html"><img src="../assets/image/slide_3.jpg" alt=""></a>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div class="swiper-button-prev"></div>-->
<!--    <div class="swiper-button-next"></div>-->
<!--    <div class="swiper-pagination"></div>-->
<!--  </div>-->
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
// Import Swiper styles
import 'swiper/css';
export default {
  name: "swiper",
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log('slide change');
    };
    return {
      onSwiper,
      onSlideChange,
    };
  },
}
</script>

<style scoped>

</style>