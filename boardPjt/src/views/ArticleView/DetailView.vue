<template>
    <div>
        <h1>DetailView</h1>
        <div v-if="article">
            <p>{{ article.title }}</p>
            <p>{{ article.content }}</p>
            <!-- 댓글 -->
            <Comments
                v-for="comment in article.comments"
                :key="article.id"
                :comment = "comment" />
            <CreateCommentForm />
        </div>
        <p v-else>게시물 읎다!</p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useBoardStore } from '@/stores/counter'
import { useRoute } from 'vue-router'
import CreateCommentForm from '@/components/comments/CreateCommentForm.vue'
import Comments from '@/components/comments/Comments.vue'
const store = useBoardStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/community/article/${route.params.id}/`
    })
    .then((response) => {
        article.value = response.data
    })
    .catch((error) => {
        console.log('세부 게시물을 가져오는 데 실패헀다!', error)
    })
})
</script>

<style lang="scss" scoped>

</style>