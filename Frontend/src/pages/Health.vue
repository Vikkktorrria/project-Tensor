<template>
  <h1 class="h1-text">Диагнозы</h1>
  <my-dialog v-model:show="dialogVisible">
    <search-diagnosis
        @filter="filter"
    ></search-diagnosis>
  </my-dialog>
  <div class="container container_only-row">
    <button class="btn" @click="dialogVisible = true">
      Поиск по дате
    </button>
    <button v-if="filterDiagnoses !== diagnoses" class="btn" @click="showAll">
      Отменить поиск
    </button>
    <list-diagnoses
        :diagnoses="filterDiagnoses"
    >
    </list-diagnoses>
  </div>
</template>

<script>
import SearchDiagnosis from "../components/Health/SearchDiagnosis";
import ListDiagnoses from "../components/Health/ListDiagnoses";
import axios from "axios";

export default {
  name: "Health",
  components: {
    SearchDiagnosis,
    ListDiagnoses
  },
  data() {
    return {
      diagnoses: [],
      filterDiagnoses: [],
      dialogVisible: false,
    }
  },
  methods: {
    filter(date) {
      this.dialogVisible = false;
      this.filterDiagnoses = this.diagnoses.filter((diagnosis) => {
        let dateDiagnosis = new Date(diagnosis.valid_date)
        return dateDiagnosis.getFullYear() + ' ' + dateDiagnosis.getMonth() + ' ' + dateDiagnosis.getDate() === date.getFullYear() + ' ' + date.getMonth() + ' ' + date.getDate()
      })
    },
    showAll() {
      this.filterDiagnoses = this.diagnoses
    },
    async fetchNews(e) {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/user/diagnoses', {
          headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
        })
        let diagnoses = response.data
        diagnoses = diagnoses.sort((a,b) => {
          return new Date(b.date_of_visit) - new Date(a.date_of_visit);
        });
        diagnoses.forEach((el) => {
          let created_on = el.date_of_visit.split('T')[0]
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
          el.valid_date = el.date_of_visit
          el.date_of_visit = day + '.' + month + '.' + year
        })
        this.filterDiagnoses = diagnoses
        this.diagnoses = [...diagnoses]
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
.btn {
  background-color: rgba(81, 148, 239, 0.6);
  color: #35538d;
  border-radius: 40px;
  padding: 5px 15px;
  -webkit-transition-duration: .4s;
  transition-duration: .4s;
  font-size: 18px;
  margin-right: 10px;
}
</style>