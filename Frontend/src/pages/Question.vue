<template>
  <div class="container container_only-row">
    <div class="row">
      <div class="accordion">
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingOne">
            <button class="accordion-button accord__title" type="button" data-bs-toggle="collapse"
                    data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true"
                    aria-controls="panelsStayOpen-collapseOne">
              Не могу вспомнить пароль
            </button>
          </h2>
          <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show"
               aria-labelledby="panelsStayOpen-headingOne">
            <div class="accordion-body accord__text">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore, voluptates
              asperiores. Quas neque ducimus odio nobis facere, a suscipit blanditiis aliquid
              voluptatibus ratione dicta optio ipsam? Repellendus atque eligendi odit!
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
            <button class="accordion-button collapsed accord__title" type="button" data-bs-toggle="collapse"
                    data-bs-target="#panelsStayOpen-collapseTwo" aria-expanded="false"
                    aria-controls="panelsStayOpen-collapseTwo">
              Не могу вспомнить e-mail
            </button>
          </h2>
          <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse"
               aria-labelledby="panelsStayOpen-headingTwo">
            <div class="accordion-body accord__text">
              Lorem ipsum dolor sit, amet consectetur adipisicing elit. Rem iusto quisquam
              nisi harum error ab deleniti veritatis culpa voluptates tempora nostrum, impedit
              doloremque aperiam laborum reiciendis hic porro sunt beatae.
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingThree">
            <button class="accordion-button collapsed accord__title" type="button" data-bs-toggle="collapse"
                    data-bs-target="#panelsStayOpen-collapseThree" aria-expanded="false"
                    aria-controls="panelsStayOpen-collapseThree">
              Хочу узнать номер телефона больницы
            </button>
          </h2>
          <div id="panelsStayOpen-collapseThree" class="accordion-collapse collapse"
               aria-labelledby="panelsStayOpen-headingThree">
            <div class="accordion-body accord__text">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut dignissimos in
              architecto debitis officiis, inventore delectus quos autem minus eius optio cum
              quia maxime illum! Libero voluptas incidunt aperiam inventore.
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingFour">
            <button class="accordion-button collapsed accord__title" type="button" data-bs-toggle="collapse"
                    data-bs-target="#panelsStayOpen-collapseFour" aria-expanded="false"
                    aria-controls="panelsStayOpen-collapseFour">
              Хочу узнать адрес больницы
            </button>
          </h2>
          <div id="panelsStayOpen-collapseFour" class="accordion-collapse collapse"
               aria-labelledby="panelsStayOpen-headingFour">
            <div class="accordion-body accord__text">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque eos et in,
              quibusdam laborum corporis placeat voluptatum eaque aperiam nihil accusantium
              facere maiores tempore. Doloremque quod pariatur neque est quae!
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import {mapMutations, mapState} from 'vuex';
export default {
  name: "Question",
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth
    }),
  }
}
</script>

<style scoped>

</style>