<template>
  <div id="app">
    <div class="chat-container">
      <div v-for="(message, index) in chatStore.messages" :key="index" class="message">
        <strong>{{ message.sender }}:</strong> {{ message.content }}
      </div>
    </div>
    <div class="input-container">
      <input v-model="userInput" @keyup.enter="handleSendMessage" placeholder="메시지를 입력하세요">
      <button @click="handleSendMessage">Send</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useBoardStore } from '@/stores/counter'

const userInput = ref('')
const chatStore = useBoardStore()

const handleSendMessage = () => {
  if (userInput.value.trim()) {
    chatStore.sendMessage(userInput.value.trim())
    userInput.value = ''
  }
}
</script>

<style scoped>
#app {
  text-align: left;
  margin-top: 60px;
}

.chat-container {
  border: 1px solid #ccc;
  padding: 10px;
  height: 300px;
  overflow-y: scroll;
  margin-bottom: 10px;
}

.message {
  margin: 5px 0;
}

.input-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

input {
  width: 70%;
  padding: 10px;
  margin-right: 10px;
}

button {
  padding: 10px 20px;
}
</style>
