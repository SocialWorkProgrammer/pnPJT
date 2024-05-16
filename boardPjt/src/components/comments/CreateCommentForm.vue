<template>
    <div>
      <p>주의 : 분탕 시 영구차단임 </p>
      <form @submit.prevent="createComment">
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
  const content = ref(null)
  const router = useRouter()
  
  const createComment = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/community/article/:id/comment`,
      data: {
        content: content.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((response) => {
        console.log(response.data)
        router.push({ name: 'DetailView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  </script>
  
  <style>
  
  </style>
  