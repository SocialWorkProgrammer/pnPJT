<template>
    <div>
      <h1>게시글 작성</h1>
      <p>악! 게시글 작성 폼에 오신 것을 환영하는 바 입니다!</p>
      <form @submit.prevent="createArticle">
        <div>
          <label for="title">제목 : </label>
          <input type="text" v-model.trim="title" id="title">
        </div>
        <div>
          <label for="content">내용 : </label>
          <textarea v-model.trim="content" id="content"></textarea>
        </div>
        <input type="submit">
      </form>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref } from 'vue'
  import { useBoardStore } from '@/stores/counter'
  import { useRouter } from 'vue-router'
  
  const store = useBoardStore()
  const title = ref(null)
  const content = ref(null)
  const router = useRouter()
  
  const createArticle = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/community/`,
      data: {
        title: title.value,
        content: content.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((response) => {
        console.log(response.data)
        router.push({ name: 'ArticleView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  </script>
  
  <style>
  
  </style>
  