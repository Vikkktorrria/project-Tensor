<template>
  <div class="row">
    <label
        class="card card_user card_no-border card_no-padding col-md-2"
        for="input__file"
    >
      <img
          v-if="!currentUser.avatarName"
          class="card_user__image"
          src="../../assets/image/user-icon.png"
          :alt="currentUser.name"
      >
      <img
          v-if="currentUser.avatarName"
          class="card_user__image"
          :src="'http://127.0.0.1:5000/user/image/' + currentUser.avatarName"
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
      <div v-if="!currentUser.isDoctor" class="card__title">
        {{currentUser.surname}} {{currentUser.name}} {{currentUser.patronymic}},
        {{currentUser.age}} {{currentUser.ageText}}
        <br>
        Email: {{currentUser.email}}
        <br>
        Телефон: {{currentUser.phone}}
      </div>
      <div v-if="currentUser.isDoctor" class="card__title">
        {{currentUser.surname}} {{currentUser.name}} {{currentUser.patronymic}},
        {{currentUser.age}} {{currentUser.ageText}}
        <br>
        Email: {{currentUser.email}}
        <br>
        Телефон: {{currentUser.phone}}
        <br>
        Специализация: {{this.doctorData.qualification}}
        <br>
        Опыт работы: {{this.doctorData.experience}}
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from "vuex";
import axios from "axios";

export default {
  name: "HeadProfile",
  data() {
    return {
      doctorData: []
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser,
      isAuth: state => state.auth.isAuth
    }),
  },
  methods: {
    ...mapActions({
      checkAuth: 'auth/checkAuth'
    }),
    async downloadFile(e) {
      try {
        let formData = new FormData();
        formData.append('file', e.target.files[0])
        const response = await axios.put('http://127.0.0.1:5000/api/user/upload/avatar', formData, {
          headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
          'Content-Type': 'multipart/form-data'
        })
        await this.checkAuth()
      } catch (error) {
        console.log(error.request.response)
      }
    },
    async fetchDoctor() {
      if(this.currentUser.isDoctor) {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/user/doctor/info', {
            headers: {Authorization: `Bearer ${localStorage.getItem('token')}`},
          })
          console.log(response.data)
          this.doctorData = response.data
        } catch (error) {
          console.log(error)
        }
      }
    }
  },
  mounted() {
    this.fetchDoctor()
  }
}
</script>

<style scoped>
.card_user {
  -webkit-box-shadow: none;
  box-shadow: none;
  width: 130px;
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