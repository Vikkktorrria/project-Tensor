<template>
  <div class="container">
    <div class="row">
      <div class="card card_user col-2">
        <img class="card_user__image" src="../assets/image/user-icon.png" alt="Татьяна">
      </div>
      <div class="card card_no-border col-md-8">
        <div class="card__title">
          Татьяна
        </div>
        <div class="card__text">
          20лет
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="row">
      <div class="card card_no-border col-md-5">
        <h3 class="card__title">
          Паспортные данные
        </h3>
        <div class="card__text">
          <form class="form form_card" onSubmit="event.preventDefault(); checkProfileForm();">
            <div class="form__el form_card__el">
              Серия:
              <input type="text" class="form__input form_card__input" id="passport-seria" name="passport-seria" placeholder="1111">
              <small>Error message</small>
            </div>
            <div class="form__el form_card__el">
              Номер:
              <input type="text" class="form__input form_card__input" id="passport-number" name="passport-number" placeholder="999999">
              <small>Error message</small>
            </div>
            <div class="form__button form_card__button">
              <button class="btn">
                Сохранить
              </button>
            </div>
          </form>
        </div>
      </div>
      <div class="card card_no-border col-md-5">
        <h3 class="card__title">
          Снилс
        </h3>
        <div class="card__text">
          <form class="form form_card" onSubmit="event.preventDefault(); checkProfileForm();">
            <div class="form__el form_card__el">
              Номер:
              <input type="text" class="form__input form_card__input" id="name" name="name" placeholder="111-222-333333">
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
  </div>
  <div class="container">
    <div class="row">
      <div class="card card_no-border col-md-11">
        <h3 class="card__title">
          Анамнез
        </h3>
        <div class="card__text">
          <form class="form form_card" onSubmit="event.preventDefault(); checkProfileForm();">
            <div class="form__el form_card__el">
              <textarea class="form__input form_card__input" name="anamnez" id="anamnez" rows="10"></textarea>
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
</template>

<script>
export default {
  name: "Profile"
}
</script>

<style scoped>

</style>