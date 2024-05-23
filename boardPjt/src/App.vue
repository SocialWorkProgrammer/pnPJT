<template>
  <div>
    <Navbar />
    <RouterView />
    <div class="character-container">
      <!-- 캐릭터 사진 -->
      <img src="@/assets/하로.jpg" class="character-image" @click="toggleChatRoom">
    </div>
    <!-- 채팅방 -->
    <ChatBot v-if="showChatRoom" class="chat"/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useBoardStore } from './stores/counter'
import SignUpView from './views/HomeView/SignUpView.vue'
import LoginView from './views/HomeView/LoginView.vue'
import LogoutView from '@/views/HomeView/LogoutView.vue'
import Navbar from '@/components/functions/Navbar.vue'
import ChatBot from './components/functions/ChatBot.vue'
const store = useBoardStore()

const showChatRoom = ref(false)

const toggleChatRoom = () => {
  showChatRoom.value = !showChatRoom.value
}

onMounted(() => {
  // 페이지가 로드되면 실행되는 로직
})
</script>

<style scoped>
.character-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
}

.character-image {
  height: 100px;
  width: 100px;
  cursor: pointer;
}
.chat {
  position : fixed;
  background-color: #EFFCEE;
  bottom : 130px;
  right : 130px;
  width: 500px;
  height: auto;
  z-index: 0;
}

</style>
