<template>
  <h1 class="h1-text">Авторизация</h1>
  <div class="content__container">
    <form-component
        v-model:formInputs="formInputs"
        v-model:buttonText="buttonText"
    ></form-component>
  </div>
</template>

<script>
export default {
  name: "Auth",
  data() {
    return {
      formInputs: [
        {
          value: '',
          errorMessage: 'Поле почта не может быть пустым',
          placeholder: 'Почта',
          type: 'text'
        },
        {
          value: '',
          errorMessage: 'Поле пароль не может быть пустым',
          placeholder: 'Пароль',
          type: 'text'
        }
      ],
      buttonText: 'Войти'
    }
  }
}
</script>

<style>

</style>