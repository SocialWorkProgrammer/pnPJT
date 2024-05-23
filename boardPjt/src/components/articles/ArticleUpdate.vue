<template>
  <div>
    <h1>게시글 수정</h1>
    <p>악! 게시글 수정 폼에 오신 것을 환영하는 바 입니다!</p>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea id="content" v-model.trim="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useBoardStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const store = useBoardStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()
const route = useRoute()

const updateArticle = function () { 
// 현재 라우터에서 게시글 ID를 가져오기
console.log(route.params.id)
axios.put(`${store.API_URL}/community/article/${route.params.id}/`, {
  title: title.value,
  content: content.value
  }, {
  headers: {
    Authorization: `Token ${store.token}`
  }
  })
  .then((response) => {
  console.log('게시물이 수정되었다!', response.data)
  router.push({ name: 'ArticleView', params: { id: articleId } }); // 수정된 게시글로 이동
  })
  .catch((error) => {
  console.log('게시물 못 수정함!', error)
  });
  }

</script>
