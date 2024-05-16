<template>
  <div>
    <h1>App.vue의 영역</h1>
    <nav>
      <RouterLink :to="{name : 'LoginView'}">[Login]</RouterLink>
      <RouterLink :to="{name : 'ArticleView'}">[Article]</RouterLink>
    </nav>
  </div>
  <RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useBoardStore } from './stores/counter'

const store = useBoardStore()
onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>

</style>
