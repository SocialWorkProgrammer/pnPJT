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
  <h1>홈 페이지</h1>
  <p>악! 홈 페이지에 오신 것을 진심으로 환영하는 바 입니다!</p>
    <nav>
    <RouterLink :to="{ name: 'CreateArticleView' }">[CREATE]</RouterLink>
    <ArticleList />
  </nav>
  </div>
</template>

<style scoped>

</style>