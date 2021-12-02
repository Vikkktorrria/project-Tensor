<template>
  <h1 class="h1-text">Новости</h1>
  <div v-if="currentUser?.isDoctor" class="form__button form__button_create form_card__button">
    <button class="btn" @click="this.dialogVisible = true">
      Создать запись
    </button>
  </div>
  <div class="container container_only-row">
    <div
        class="row"
        v-for="item in news"
        :key="item.id"
    >
      <div class="card card_no-border col-md-8" href="#">
        <h3 class="card__title">{{item.title}}</h3>
        <div class="card__pic" v-if="item.article_img">
          <img
            :src="'http://127.0.0.1:5000/user/image/' + item.article_img"
            :alt="item.title"
            class="card__pic-image">
        </div>
        <div class="card__text">
          {{item.text}}
        </div>
        <div class="card__footer">
          <div class="card__date">
            {{item.created_on}}
          </div>
          <div v-if="currentUser?.isDoctor" class="news__buttons">
            <div class="form__button form_card__button">
              <button class="btn">
                Редактировать
              </button>
            </div>
            <div class="form__button form_card__button">
              <button class="btn" @click="deleteNews(item.id)">
                Удалить
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <my-dialog v-model:show="dialogVisible">
    <create-article
        @create="createNews"
    ></create-article>
  </my-dialog>
</template>

<script>
import axios from "axios";
import {mapState} from "vuex";
import CreateArticle from "../components/CreateArticle";

export default {
  components: [
    CreateArticle,
  ],
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
        this.news = [...this.news, ...response.data]
      } catch (error) {
        alert(error.request.response)
      } finally {

      }
    },
    async createNews(e) {
      this.dialogVisible = false;
      await this.fetchNews()
    },
    async updateNews(e) {
      try {
        const response = await axios.put('http://127.0.0.1:5000/api/news')
      } catch (error) {
        alert(error.request.response)
      } finally {
        await this.fetchNews()
      }
    },
    async deleteNews(article_id) {
      if(confirm('Вы действительно хотите удалить запись?')) {
        try {
          const response = await axios.delete(`http://127.0.0.1:5000/api/user/delete/article/${article_id}`, {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
          })
        } catch (error) {
          alert(error.request.response)
        } finally {
          await this.fetchNews()
        }
      }
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
.news__buttons {
  display: flex;
}
.card__footer {
  display: flex;
  justify-content: space-between;
}
</style>