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
import {mapActions, mapState} from "vuex";
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
      article: [],
    }
  },
  methods: {
    ...mapActions({
      fetchNews: 'news/fetchNews'
    }),
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
      news: state => state.news.news
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