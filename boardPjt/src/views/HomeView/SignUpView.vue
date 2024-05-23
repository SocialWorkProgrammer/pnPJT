<template>
  <div class="wrapper">
    <div class="formcontent">
      <h1>회원가입 페이지</h1>
      <form @submit.prevent="signUp" class="signup-form">
        <div class="input-group">
          <label for="username">Username:</label>
          <input type="text" v-model.trim="username" id="username" />
        </div>
        <div class="input-group">
          <label for="password1">Password:</label>
          <input type="password" v-model.trim="password1" id="password1" />
        </div>
        <div class="input-group">
          <label for="password2">Password Confirmation:</label>
          <input type="password" v-model.trim="password2" id="password2" />
        </div>
        <div class="input-group">
          <label for="name">Name:</label>
          <input type="text" v-model.trim="name" id="name" />
        </div>
        <input type="submit" class="submit-btn" value="회원가입" />
      </form>
    </div>
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

.signup-form {
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
