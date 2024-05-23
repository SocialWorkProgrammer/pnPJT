<template>
  <div>
    <h1>댓글 수정</h1>
    <p>악! 댓글 수정 폼에 오신 것을 환영하는 바 입니다!</p>
    <form @submit.prevent="updateComment" class="comment-form">
      <div class="form-group">
        <label for="content" class="label">내용 :</label>
        <input id="content" v-model.trim="content" class="input"></input>
      </div>
      <button type="submit" class="submit-btn">댓글 수정</button>
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

const updateComment = function () { 
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
    console.log('댓글 못 수정함!', error)
  });
}
</script>

<style scoped>
.comment-form {
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 1rem;
}

.label {
  font-weight: bold;
}

.input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.submit-btn {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #0056b3;
}
</style>
