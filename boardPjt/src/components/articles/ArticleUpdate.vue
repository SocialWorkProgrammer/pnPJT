<template>
  <div class="wrapper">
    <div class="formcontent">
      <h1>게시글 수정</h1>
      <form @submit.prevent="updateArticle" class="update-article-form">
        <div class="input-group">
          <label for="title">제목</label>
          <input type="text" v-model.trim="title" id="title" placeholder="제목은 30자 미만">
        </div>
        <div class="input-group">
          <label for="content">내용</label>
          <textarea id="content" v-model.trim="content" placeholder="내용에 정치적, 모욕적인 내용을 넣으면 정지당할 수 있습니다"></textarea>
        </div>
        <input type="submit" class="submit-btn" value="제출">
      </form>
    </div>
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
    router.push({ name: 'ArticleView', params: { id: route.params.id } }); // 수정된 게시글로 이동
  })
  .catch((error) => {
    console.log('게시물 못 수정함!', error)
  });
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

.wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f7f9fc;
  min-height: 100vh;
  font-family: 'Roboto', sans-serif;
}

.formcontent {
  padding: 3rem;
  margin: 3rem;
  border-radius: 15px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 100%;
  max-width: 800px;
}

h1 {
  margin-bottom: 1.5rem;
  font-size: 2rem;
  color: #333333;
}

p {
  margin-bottom: 2rem;
  font-size: 1.25rem;
  color: #555555;
}

.update-article-form {
  font-size: 16px;
  width: 100%;
}

.input-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

.input-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #555555;
  font-weight: 500;
}

.input-group input,
.input-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #dddddd;
  border-radius: 5px;
  font-size: 1rem;
  color: #333333;
  transition: border-color 0.3s;
}

.input-group input:focus,
.input-group textarea:focus {
  border-color: #0066cc;
  outline: none;
}

.submit-btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: #0066cc;
  color: #ffffff;
  font-size: 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.submit-btn:hover {
  background-color: #004999;
  box-shadow: 0 4px 8px rgba(0, 102, 204, 0.3);
}
</style>
