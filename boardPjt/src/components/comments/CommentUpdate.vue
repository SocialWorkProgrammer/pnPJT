<template>
  <div>
    <h1>댓글 수정</h1>
    <p>악! 댓글 수정 폼에 오신 것을 환영하는 바 입니다!</p>
    <form @submit.prevent="updateComment">
      <div>
        <label for="content">내용 : </label>
        <input id="content" v-model.trim="content"></input>
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
const content = ref(null)
const router = useRouter()
const route = useRoute()

const updateComment = function (commentId) { 
// 현재 라우터에서 댓글 ID를 가져오기
console.log(route.params)
axios.put(`${store.API_URL}/community/article/${route.params.id}/comment/${route.params.commentId}/`, {
  content: content.value
  }, {
  headers: {
    Authorization: `Token ${store.token}`
  }
  })
  .then((response) => {
  console.log('댓글이 수정되었다!', response.data)
  router.push({ name: 'DetailView', params: { id: route.params.id } }); // 수정된 게시글로 이동
  })
  .catch((error) => {
  console.log('댓글  못 수정함!', error)
  });
  }

</script>
