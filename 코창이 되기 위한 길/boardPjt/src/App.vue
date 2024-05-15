<template>
  <div>
    <h1>살려줘</h1>
    <RouterLink :to="{name : 'LoginView'}">[Login]</RouterLink>
  </div>
  <RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useBoardStore } from './stores/counter';

const store = useBoardStore()
onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>

</style>
