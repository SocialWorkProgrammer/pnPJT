<template>
    <div>
        <h1>DetailView</h1>
        <div v-if="article">
        <p>{{ article.id }}</p>
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useBoardStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useBoardStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/article/$${route.params.id}/`
    })
    .then((response) => {
        article.value = response.data
    })
    .catch((error) => {
        console.log(error)
    })
})
</script>

<style lang="scss" scoped>

</style>