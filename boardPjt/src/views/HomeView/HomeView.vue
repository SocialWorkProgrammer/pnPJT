<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import ArticleList from '@/components/articles/ArticleList.vue'
</script>

<template>
  <div>
    <RouterLink :to="{ name: 'CreateArticleView' }">[CREATE]</RouterLink>
    <ArticleList />
  </div>
</template>

<style scoped>

</style>