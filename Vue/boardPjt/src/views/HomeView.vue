<script setup>
import { RouterView, RouterLink } from 'vue-router'
import getArticles from '@/components/getArticles.vue'
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
    <RouterLink :to="{ name: 'CreateArticleView' }">[CREATE]</RouterLink>
    <getArticles />
  </div>
</template>

<style scoped>

</style>