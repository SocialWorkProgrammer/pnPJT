<template>
    <div>
        <RouterLink
        :to="{ name: 'DetailView', params: {id: article.id}}">[DETAIL]</RouterLink>
        <h1>제목 : {{ article.title }}</h1>
        <!-- <p>글 번호 : {{ article.id }}</p> -->
        <p> {{ article.content }}</p>
        <p>{{ article.comment }}</p>
    </div>
</template>

<script setup>
import {RouterLink} from 'vue-router'
defineProps({
    article: Object
})
</script>

<style lang="scss" scoped>

</style>