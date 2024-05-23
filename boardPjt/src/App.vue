<template>
  <Navbar />
    <RouterView />
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
</style>
