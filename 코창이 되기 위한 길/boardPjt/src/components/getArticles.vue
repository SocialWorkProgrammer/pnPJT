<template>
    <div>
        <h1>게시판.</h1>
        <h2>주의 : 분탕치다 걸리면 영구차단임</h2>
        <getArticleItem 
        v-for="article in store.articles"
        :key="article.id"
        :article="article" />
    </div>
</template>

<script setup>
import { useBoardStore } from '@/stores/counter'
import getArticleItem from './getArticleItem.vue'
const store = useBoardStore()
</script>


<style lang="scss" scoped>

</style>