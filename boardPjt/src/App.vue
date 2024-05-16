<template>
  <div>
    <h1>App.vue의 영역</h1>
    <p>현재 로그인 상태 : {{ store.isLogin }}</p>
        <RouterLink :to="{name : 'SignUpView'}">[SignUp]</RouterLink>
        <RouterLink :to="{name : 'LoginView'}">[Login]</RouterLink>
      <RouterLink :to="{name : 'ArticleView'}">[Article]</RouterLink>
      <LogoutView/>
  </div>
  <RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useBoardStore } from './stores/counter'
import LogoutView from '@/views/HomeView/LogoutView.vue'
const store = useBoardStore()
onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>

</style>
