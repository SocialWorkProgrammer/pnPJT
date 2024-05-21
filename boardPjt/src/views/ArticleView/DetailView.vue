<template>
    <div>
        <div v-if="article">
            <p>제목 : {{ article.title }}</p>
            <p>내용 : {{ article.content }}</p>
            <!-- 게시물 시리얼라이저 확인용 -->
            <!-- <p>{{ article }}</p> -->
            <!-- 댓글 -->
            <h3>댓글창입니다. 에티켓 지켜주세요.</h3>
            <Comments
                v-for="comment in article.comments"
                :key="article.id"
                :comment = "comment" />
            <CreateCommentForm />
            <p>{{ route.params }}</p>
            <v-btn
                class="mr-2"
                size="small"
                variant="tonal"
                color="green"
                @click="UpdateArticle">
                게시글 수정
            </v-btn>
            <v-btn
                class="mr-2"
                size="small"
                variant="tonal"
                color="red"
                @click="deleteArticle">
                게시글 삭제
            </v-btn>

        </div>
        <p v-else>게시물 읎다!</p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useBoardStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CreateCommentForm from '@/components/comments/CreateCommentForm.vue'
import Comments from '@/components/comments/Comments.vue'

const store = useBoardStore()
const route = useRoute()
const router = useRouter()
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
  
  const UpdateArticle = () => {
      router.push({ name: 'ArticleUpdate', params: { id: route.params.id }})
    }

  const deleteArticle = () => {
    if (window.confirm('정말 삭제하시겠습니까?')) {
      axios({
        method: 'delete',
        url: `${store.API_URL}/community/article/${route.params.id}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
        .then((response) => {
          console.log('게시글이 삭제됨!', response)
          router.go(-1) // 현재 페이지 새로고침
        })
        .catch((error) => {
          console.log('게시글이 삭제되지 않았습니다.', error)
        })
    }
  }



</script>

<style scoped>

</style>