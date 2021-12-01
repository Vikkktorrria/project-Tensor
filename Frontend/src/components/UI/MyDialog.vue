<template>
  <div class="dialog" v-if="show" @click="hideDialog">
    <div @click.stop class="dialog__content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import toggleMixin from "../../mixins/toggleMixin";

export default {
  name: "my-dialog",
  mixins: [toggleMixin]
}
</script>

<style scoped>
.dialog {
  z-index: 10;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgba(53, 83, 141, 0.7);
  position: fixed;
  display: flex;
}

.dialog__content {
  border-radius: 5px;
  color: #35538d;
  margin: auto;
  padding: 20px 20px 10px;
  background: white;
  min-height: 150px;
  min-width: 300px;
}
</style>