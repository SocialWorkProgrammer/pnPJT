<template>
  <div class="row">
    <div class="account-form col-4">
      <div v-if="store.isLogin">
        <RouterLink :to="{ name: 'ProfileView', params: {username : store.state.username }}"><p>어서오세요! {{ store.state.username }}</p></RouterLink>
        <LogoutView class="menu-item" />
      </div>
      <div v-else>
        <RouterLink :to="{ name: 'SignUpView' }" class="menu-item">[회원가입]</RouterLink>
        <RouterLink :to="{ name: 'LoginView'}" class="menu-item">[로그인]</RouterLink>
      </div>
    </div>
    <Navbar />
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
const store = useBoardStore()

</script>

<style scoped>
.account-form {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.menu-item {
  margin: 0 10px; /* 메뉴 아이템 간격 조정 */
}
</style>
