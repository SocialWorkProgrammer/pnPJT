<template>
    <div>
        <h1>게시판에 온 것을 환영한다!</h1>
        <h2>경고 : 분탕치다 걸리면 영구차단임</h2>
        <RouterLink :to="{ name: 'CreateArticleView' }">[CREATE]</RouterLink>
        <ArticleList />
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/counter'
import ArticleList from '../components/ArticleList.vue'
const store = useBoardStore()

onMounted(() => {
    store.getArticles()
})
</script>


<style lang="scss" scoped>

</style>