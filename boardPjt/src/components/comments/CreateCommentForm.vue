<template>
    <div>
      <p>댓글 작성란입니다.</p>
      <form @submit="createComment" class="comment">
        <div>
          <label for="content">내용 : </label>
          <input v-model.trim="content" id="content"></input>
        </div>
        <input type="submit">
      </form>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref } from 'vue'
  import { useBoardStore } from '@/stores/counter'
  import { useRoute, useRouter } from 'vue-router'
  
  const store = useBoardStore()
  const content = ref(null)
  const route = useRoute()
  const router = useRouter()
  
  const createComment = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/community/article/${route.params.id}/comment/`,
      data: {
        content: content.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((response) => {
        console.log(response.data)
        // router.push({ name: 'DetailView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  </script>
  
  <style scoped>
  .comment{
    border: 1px solid black;
    
  }
  </style>
  