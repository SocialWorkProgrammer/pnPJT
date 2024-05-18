<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/counter'

const store = useBoardStore()

onMounted(() => {
  store.getArticles()
})

</script>

<template>
  <div>
    <RouterLink :to="{ name: 'CreateArticleView' }">[CREATE]</RouterLink>
    <ArticleList />
  </div>
</template>

<style scoped>

</style>