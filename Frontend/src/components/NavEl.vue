<template>
  <a
      :class="{
        'navigation__el': !isActive,
        'navigation__el active': isActive
      }"
  >
    <div :class="'navigation__icon ' + classIcon" >
    </div>
    <div class="navigation__text">
      <slot></slot>
    </div>
  </a>
</template>

<script>
export default {
  name: "NavEl",
  props: {
    isActive: {
      type: Boolean,
      required: true
    },
    classIcon: {
      type: String,
      required: true
    }
  },
}
</script>

<style  lang="scss" src="@/assets/style/style.scss"></style>