<template>
  <div class="main-container">
    <Nav></Nav>
    <router-view></router-view>
    <div class="footer"></div>
  </div>
</template>

<script setup>
import Nav from './views/components/Nav.vue'
</script>

<style lang="less">
.main-container {
  height: 100vh;
  .footer {
    height: 100px;
  }
}
</style>
