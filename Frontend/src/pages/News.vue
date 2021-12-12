<template>
  <h1 class="h1-text">Новости</h1>
  <div v-if="currentUser?.isDoctor" class="form__button form__button_create form_card__button">
    <button class="btn" @click="this.dialogVisible = true">
      Создать запись
    </button>
  </div>
  <div class="container container_only-row">
    <Article
        v-for="item in news"
        :key="item.id"
        :item="item"
        @update="updateArticle"
        @delete="deleteArticle"
    ></Article>
  </div>
  <my-dialog v-model:show="dialogVisible">
    <create-article
        @create="createArticle"
    ></create-article>
  </my-dialog>
</template>

<script>
import axios from "axios";
import {mapState} from "vuex";
import CreateArticle from "../components/News/CreateArticle";
import Article from "../components/News/Article";

export default {
  components: {
    Article,
    CreateArticle,
  },
  name: "News",
  data() {
    return {
      dialogVisible: false,
      news: [],
      article: [],
    }
  },
  methods: {
    async fetchNews(e) {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/news')
        let news = response.data
        news = news.sort((a,b) => {
          return new Date(b.created_on) - new Date(a.created_on);
        });
        news.forEach((el) => {
          let created_on = el.created_on.split('T')[0]
          created_on = created_on.split('-')
          let day = created_on[2]
          let month = created_on[1]
          let year = created_on[0]
          if (day.split('')[0] === '0') {
            day = day.split('')[1]
          }
          if (month.split('')[0] === '0') {
            day = month.split('')[1]
          }
          el.created_on = day + '.' + month + '.' + year
        })
        this.news = news
      } catch (error) {
        console.log(error)
      }
    },
    async createArticle(e) {
      this.dialogVisible = false;
      setTimeout(async () => {
        await this.fetchNews()
      }, 1500)
    },
    updateArticle(e) {
      setTimeout(async () => {
        await this.fetchNews()
      }, 1500)
    },
    async deleteArticle(e) {
      await this.fetchNews()
    },
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
    }),
  },
  mounted() {
    this.fetchNews()
  }
}
</script>

<style scoped>
.form__button.form__button_create {
  display: flex;
  justify-content: start;
}
.form__button {
  display: flex;
  justify-content: end;
  margin-left: 10px;
}
</style>