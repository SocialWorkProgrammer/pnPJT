<template>
    <div>
        <ArticleListItem 
        v-for="article in store.articles"
        :key="article.id"
        :article="article" />
    </div>
</template>

<script setup>
import { useBoardStore } from '@/stores/counter'
import ArticleListItem from '@/components/articles/ArticleListItem.vue'
const store = useBoardStore()
</script>


<style lang="scss" scoped>

</style>