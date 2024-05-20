<template>
  <div>
    <h1>App.vue의 영역</h1>
    <RouterLink :to="{ name: 'SignUpView' }">[회원가입]</RouterLink>
    <RouterLink :to="{ name: 'LoginView'}">[로그인]</RouterLink>
    <LogoutView />
    <p>{{ store.isLogin }}</p>
    <p>{{  store.token }}</p>
    <Navbar />
    <!-- <Article /> -->
    <RouterView />
  </div>
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useBoardStore } from './stores/counter'
import SignUpView from './views/HomeView/SignUpView.vue'
import LoginView from './views/HomeView/LoginView.vue'
import LogoutView from '@/views/HomeView/LogoutView.vue'
import Navbar from '@/components/functions/Navbar.vue'
import Article from './components/functions/Article.vue'
const store = useBoardStore()
</script>

<style scoped>


</style>
