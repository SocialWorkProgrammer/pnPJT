<template>
    <div>
    <h1>로그인 페이지</h1>
    <!-- 로그인 폼 -->
    <form @submit.prevent="logIn">
      <div>
        <label for="username">username : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password">password : </label>
        <input type="password" v-model.trim="password" id="password">
      </div>
      <input type="submit" value="logIn">
    </form>

    </div>
</template>

<script setup>
// ref와 store import
import { ref } from 'vue'
import { useBoardStore } from '@/stores/counter'
// id, pw, store 변수 선언
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

</style>