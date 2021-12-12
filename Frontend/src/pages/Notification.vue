<template>
  <div class="container">
    <carousel
        class="slider"
        :wrapAround="true"
        :autoplay="2500"
    >
      <slide v-for="article in news.slice(0, 3)" :key="article.id">
        <div class="slide__el">
          <img
              @click="$router.push('/news')"
              class="slide_img"
              :src="'http://127.0.0.1:5000/user/image/' + article.article_img"
              :alt="article.title">
          <p class="slide__text">{{article.title}}</p>
        </div>
      </slide>
      <template #addons>
        <navigation />
      </template>
    </carousel>
    <div class="row">
      <a
          @click="$router.push('/profile')"
          class="card col-md-4"
      >
        <h3 class="card__title">
          Мой профиль
        </h3>
        <div class="card__text">
          Профиль заполнен на {{percent}}%
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
          Создайде запись
        </div>
      </a>
    </div>
  </div>
</template>

<script>
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';
import {mapActions, mapState} from "vuex";
import axios from "axios";
export default {
  name: "Notification",
  data() {
    return {
      percent: 0,
    }
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth,
      currentUser: state => state.auth.currentUser,
      news: state => state.news.news
    }),
  },
  methods: {
    ...mapActions({
      fetchNews: 'news/fetchNews'
    }),
    percentProfile() {
      if(this.currentUser.passport.number) {
        this.percent += 25
      }
      if(this.currentUser.anamnesis) {
        this.percent += 25
      }
      if(this.currentUser.snils) {
        this.percent += 25
      }
      if(this.currentUser.avatarName) {
        this.percent += 25
      }
    }
  },
  mounted() {
    this.fetchNews()
    this.percentProfile()
  }
}
</script>

<style>
.carousel__prev, .carousel__next {
  background-color: #4c7fe6;
}
.slider {
  margin: 10px;
}
.slide__el {
  position: relative;
}
.slide__text {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 50px;
  color: white;
  font-size: 24px;
  background-color: rgba(89, 137, 232, 0.7);
  border-radius: 5px;
}
.slide_img {
  border-radius: 5px;
  width: 100%;
}
</style>