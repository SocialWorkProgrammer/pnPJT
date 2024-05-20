<template>
    <div>
      <h1>회원가입 페이지</h1>
      <form @submit.prevent="signUp" class="form">
        <div>
          <label for="username">username : </label>
          <input type="text" v-model.trim="username" id="username">
        </div>
        <div>
          <label for="password1">password : </label>
          <input type="password" v-model.trim="password1" id="password1">
        </div>
        <div>
          <label for="password2">password confirmation: </label>
          <input type="password"  v-model.trim="password2" id="password2">
        </div>
        <div>
          <label for="name">name: </label>
          <input type="text"  v-model.trim="name" id="name">
        </div>
        <input type="submit">
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useBoardStore } from '@/stores/counter'
  
  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const name = ref(null)
  const store = useBoardStore()
  
  const signUp = function () {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      name: name.value
    }
    store.signUp(payload)
  }
  </script>
  
  <style scoped>
  .form {
    border: 1px solid aquamarine;
  }
  </style>
  