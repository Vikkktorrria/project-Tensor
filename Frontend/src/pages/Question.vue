<template v-if="!isAuth">

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