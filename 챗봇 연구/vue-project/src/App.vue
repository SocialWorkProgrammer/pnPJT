<template>
  <div id="app">
    <div id="chat-container">
      <div id="chat-messages">
        <div v-for="(message, index) in messages" :key="index" class="message">
          {{ message.sender }}: {{ message }}
        </div>
      </div>
      <div id="user-input">
        <input type="text" v-model="userInput" @keydown.enter="sendMessage" placeholder="메시지를 입력하세요..." />
        <button @click="sendMessage">전송</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      messages: [],
      userInput: ''
    };
  },
  methods: {
    async sendMessage() {
      if (!this.userInput.trim()) return;
      this.messages.push({ sender: '나', content: this.userInput.trim() });

      try {
        const response = await axios.post('http://127.0.0.1:8000/ChatBot/chat/', { message: this.userInput.trim() });
        const chatbotResponse = response; // 이 부분 수정
        this.messages.push({ sender: '챗봇', content: chatbotResponse });
      } catch (error) {
        console.error('There was an error!', error);
        this.messages.push({ sender: 'Error', content: 'Failed to get response from the server.' });
      }

      this.userInput = '';
    }
  }
};
</script>

<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
.message {
  border-top: 1px solid #ccc;
  padding: 10px;
  margin-top: 5px;
  background-color: #e6e6e6;
}
#chat-container {
  width: 400px;
  height: 600px;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
}
#chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column-reverse;
}
#user-input {
  display: flex;
  padding: 10px;
}
#user-input input {
  flex: 1;
  padding: 10px;
  outline: none;
}
#user-input button {
  border: none;
  background-color: #1e88e5;
  color: white;
  padding: 10px 15px;
  cursor: pointer;
}
</style>
