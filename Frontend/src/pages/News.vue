<template>
  <h1 class="h1-text">Новости</h1>
  <div class="container container_only-row">
    <div
        class="row"
        v-for="item in news"
        :key="item.id"
    >
      <div class="card card_no-border col-md-8" href="#">
        <h3 class="card__title">{{item.title}}</h3>
        <div class="card__pic" v-if="item.image">
          <img
            :src="item.image"
            :alt="item.title"
            class="card__pic-image">
        </div>
        <div class="card__text">
          {{item.text}}
        </div>
        <div class="card__footer">
          <div class="card__date">
            {{item.date}}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "News",
  data() {
    return {
      news: [
        {
          id: 1,
          title: 'Новость 1',
          image: '',
          text: `Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto assumenda consequatur
          obcaecati distinctio sint minima porro saepe nisi dolor fugit tempore dolores magni
          enim, recusandae neque voluptas et sunt veniam?`,
          date: '2020-12-31'

        },
        {
          id: 2,
          title: 'Новость 2',
          image: '',
          text: `Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto assumenda consequatur
          obcaecati distinctio sint minima porro saepe nisi dolor fugit tempore dolores magni
          enim, recusandae neque voluptas et sunt veniam?`,
          date: '2020-12-31'

        },
      ]
    }
  },
  methods: {
    async fetchNews(e) {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/news')
        console.log(response)
        this.news = [...this.news, ...response.data]
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