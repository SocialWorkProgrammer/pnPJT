<template>
    <div>
        <h1>제목 : {{article.title}}</h1>
        <p>내용 : {{ article.content }}</p>
        <RouterLink
        :to="{ name: 'DetailView', params: {id: article.id}}">[DETAIL]</RouterLink>
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