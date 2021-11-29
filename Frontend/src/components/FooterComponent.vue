<template>
  <footer class='footer row'>
    <p class="footer__text">
      Сайт разработан командой SVET
    </p>
    <p class="footer__text">
      2021
    </p>
  </footer>
</template>

<script>
export default {
  name: "FooterComponent"
}
</script>

<style scoped lang="css" >
.footer {
  margin-bottom: 20px;
}
.footer__text {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>