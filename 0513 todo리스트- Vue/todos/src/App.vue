<script setup>
import { RouterLink, RouterView } from 'vue-router'
import TodoView from './views/TodoView.vue'
</script>

<template>
    <nav>
      <RouterLink to="/">Home</RouterLink>
    </nav>
  <RouterView />
</template>

<style scoped>

</style>