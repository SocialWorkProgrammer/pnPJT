<template>
    <div class="wrapper">
        <div v-if="article" class="article-content">
            <h2>제목 : {{ article.title }}</h2>
            <h4>내용 : {{ article.content }}</h4>
            <!-- 게시물 시리얼라이저 확인용 -->
            <!-- <p>{{ article }}</p> -->
            <!-- 댓글 -->
            <div class="comment-content">
            <hr>
            <div class="comment-title">
            <img src="@/assets/댓글.png" alt="#" class="comment-img">
            <h5>댓글</h5></div>
            <Comments
                v-for="comment in article.comments"
                :key="article.id"
                :comment = "comment" />
            <CreateCommentForm />
          </div>
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
        <p v-else>게시물을 찾을 수 없습니다</p>
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
  .wrapper {
    display: flex;
    justify-content: center;
    background-color: #f7f9fc;
    min-height: 100vh;
    font-family: 'Roboto', sans-serif;
  }
  
  .article-content {
    padding: 3rem;
    margin: 3rem;
    border-radius: 15px;
    background-color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: left;
    width: 100%; /* 전체 너비 설정 */
    max-width: 1200px; /* 최대 너비 설정 */
  }
  .comment-content {
    margin: 1rem 0rem;
  }
  .comment-img {
    width: 30px;
    height: 30px;
    margin: 0 4px;
  }
  .comment-title {
    display:flex;
  }
  h1 {
    margin-bottom: 1.5rem;
    font-size: 2rem;
    color: #333333;
  }
</style>