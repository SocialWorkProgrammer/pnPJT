<template>
    <div>
      <form @submit="createComment" class="comment-form">
        <div>
          <label for="content">댓글 작성 </label>
          <input v-model.trim="content" id="content" class="comment-input" placeholder="enter키를 누르면 입력됨"></input>
        </div>
        <input type="submit" class="submit-btn">
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
  .comment-form{
    border: 1px solid #ccc;
    padding: 1rem;
    border-radius: 5px;
    background-color: #f9f9f9;
    font-size: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .submit-btn{
    padding: 0.5rem 0.5rem;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 15px;
    transition: background-color 0.3s;
  }
  .comment-input{
    border : 3px solid gray;
    padding : 10px;
    border-radius : 5px;
    margin-left: 10px;
    width : auto;
    height: 100%;
    font-size: 25px;
  }
  </style>
  