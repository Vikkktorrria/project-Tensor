<template v-if="isAuth">
  <div class="container">
    <div class="row">
      <label
          class="card card_user card_no-border card_no-padding col-md-2"
          for="input__file"
      >
        <img
            v-if="!currentUser.avatar"
            class="card_user__image"
            src="../assets/image/user-icon.png"
            :alt="currentUser.name"
        >
        <img
            v-if="currentUser.avatar"
            class="card_user__image"
            :src="currentUser.avatar"
            :alt="currentUser.name"
        >
        <input
            id="input__file"
            type="file"
            style="display: none"
            accept="image/jpeg,image/png"
            name="file"
            placeholder="Фото"
            @change="downloadFile"
        />
      </label>
      <div class="card card_no-border col-md-8">
        <div class="card__title">
          {{currentUser.name}} {{currentUser.surname}} {{currentUser.patronymic}},
          {{currentUser.age}} {{currentUser.ageText}}
          <br>
          Email: {{currentUser.email}}
          <br>
          Телефон: {{currentUser.phone}}
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="row">
      <passport-form></passport-form>
      <snils-form></snils-form>
    </div>
  </div>
  <div class="container">
    <div class="row">
      <anamnesis-form></anamnesis-form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PassportForm from "../components/PassportForm";
import SnilsForm from "../components/SnilsForm";
import AnamnesisForm from "../components/AnamnesisForm";
import {mapState} from "vuex";
export default {
  name: "Profile",
  components: {
    PassportForm,
    SnilsForm,
    AnamnesisForm
  },
  data() {
    return {
      age: ''
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
      isAuth: state => state.auth.isAuth
    })
  },
  methods: {
    async downloadFile(e) {
      try {
        let formData = new FormData();
        formData.append('file', e.target.files[0])
        axios.put('http://127.0.0.1:5000/api/user/avatar', formData, {
          headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
          'Content-Type': 'multipart/form-data'
        })
      } catch (error) {
        alert(error.request.response)
      } finally {

      }
    },
  },

}
</script>

<style scoped>
.card_user {
  -webkit-box-shadow: none;
  box-shadow: none;
  width: 120px;
  height: 130px;
}
.card_user:hover {
  box-shadow: 0px 0px 12px 4px rgba(34, 60, 80, 0.4)
}
.card_no-padding {
  padding: 0;
}
.card_no-border {
  /*box-shadow: none;*/
}
.card_user__image {
  background: none;
  border-radius: 5px;
  width: 100%;
  height: 100%;
}
</style>