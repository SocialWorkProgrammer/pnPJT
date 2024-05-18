<template>
  <div class="wrapper">
    <div class="formcontent">
      <h1>로그인 페이지</h1>
      <form @submit.prevent="logIn" class="login-form">
        <div class="input-group">
          <label for="username">아이디 : </label>
          <input type="text" v-model.trim="username" id="username">
        </div>
        <div class="input-group">
          <label for="password">비밀번호 : </label>
          <input type="password" v-model.trim="password" id="password">
        </div>
        <button class="submit-btn">로그인</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useBoardStore } from '@/stores/counter'

const username = ref(null)
const password = ref(null)
const store = useBoardStore()

const logIn = function() {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
  console.log(payload)
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
}

h1 {
  margin-bottom: 1.5rem;
  font-size: 2rem;
  color: #333333;
}

.login-form {
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

.input-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #dddddd;
  border-radius: 5px;
  font-size: 1rem;
  color: #333333;
  transition: border-color 0.3s;
}

.input-group input:focus {
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
