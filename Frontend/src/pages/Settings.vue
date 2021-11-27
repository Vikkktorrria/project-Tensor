<template v-if="isAuth">
  <h1 class="h1-text">Настройки</h1>
  <div class="container">
    <div class="row">
      <div class="card card_no-border col-md-12">
        <h3 class="card__title">
          Пароль
        </h3>
        <div class="card__text">
          <form class="form form_card" onSubmit="event.preventDefault(); checkProfileForm();">
            <div class="form__el form_card__el">
              <div class="form__el-text">
                Новый пароль:
              </div>
              <input type="text" class="form__input form_card__input form_card__input-settings" id="name" name="name" placeholder="******">
              <small>Error message</small>
            </div>
            <div class="form__el form_card__el">
              <div class="form__el-text">
                Повторите пароль:
              </div>
              <input type="text" class="form__input form_card__input form_card__input-settings" id="name" name="name" placeholder="******">
              <small>Error message</small>
            </div>
            <div class="form__button form_card__button">
              <button class="btn">
                Изменить
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="card card_no-border col-md-12">
        <h3 class="card__title">
          E-mail
        </h3>
        <div class="card__text">
          <form class="form form_card" onSubmit="event.preventDefault(); checkProfileForm();">
            <div class="form__el form_card__el">
              <div class="form__el-text">
                Введите почту:
              </div>
              <input type="text" class="form__input form_card__input form_card__input-settings" id="name" name="name" placeholder="name@mail.ru">
              <small>Error message</small>
            </div>
            <div class="form__button form_card__button">
              <button class="btn">
                Изменить
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="card card_no-border col-md-12">
        <h3 class="card__title">
          Уведомления
        </h3>
        <div class="card__text">
          <form class="form form_card" onSubmit="event.preventDefault(); checkProfileForm();">
            <div class="form__el form_card__el form__el_checkbox">
              <input type="checkbox" class="form_card__checkbox" id="name" name="name" placeholder="Введите новый пароль">
              Отправлять уведомления на почту
            </div>
            <div class="form__button form_card__button">
              <button class="btn">
                Изменить
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

  </div>
  <div class="form__button">
    <button
        class="btn"
        @click="logout"
    >
      Выйти
    </button>
  </div>
</template>

<script>
import {mapMutations, mapState} from 'vuex';
export default {
  name: "Settings",
  methods: {
    ...mapMutations({
      setAuth: 'auth/setAuth'
    }),
    logout() {
      this.setAuth(false)
      localStorage.clear();
      this.$router.push({ name: 'auth' });
    }
  },
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth
    }),
  }
}
</script>

<style scoped>

</style>