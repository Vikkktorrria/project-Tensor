<template>
  <div
      class="row"
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
          <button class="btn" @click="this.dialogUpdateVisible = true">
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
  <my-dialog v-model:show="dialogUpdateVisible">
    <update-article
        :article="item.id"
        @create="updateNews"
    ></update-article>
  </my-dialog>
</template>

<script>
import UpdateArticle from "./UpdateArticle";
import axios from "axios";
import {mapState} from "vuex";

export default {
  name: "Article",
  components: {
    UpdateArticle,
  },
  data() {
    return {
      dialogUpdateVisible: false,
    }
  },
  props: {
    item: {
      type: Array,
      required: true,
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
    }),
  },
  methods: {
    async updateNews(e) {
      this.dialogUpdateVisible = false;
      this.$emit('update', true)
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
          this.$emit('delete', true)
        }
      }
    },
  },
}
</script>

<style scoped>

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