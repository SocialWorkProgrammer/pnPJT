import { ref, computed, reactive } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'

export const useBoardStore = defineStore('board', () => {
  const articles = ref([])
  const messages = ref([])
  const token = ref("")
  const API_URL = "http://127.0.0.1:8000"
  const router = useRouter()
  const route = useRoute()

  // 게시글 가져오기
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      console.log('게시물을 가져오는데 성공했다!', response)
      articles.value = response.data
    })
    .catch((error) => {
      console.log('게시물을 가져오는데 실패했다!', error)
    })
  }
  
  // 회원가입 폼
  const signUp = function (payload) {
    const { username, password1, password2, name } = payload
    axios({
      method : 'post',
      url: `${API_URL}/accounts/signup/`,
      data : {
        username, password1, password2, name
      }
    })
    .then((response) => {
      console.log('회원가입 성공!')
      const password = password1
      logIn({ username, password })
    })
    .catch((error) => {
      console.log('회원가입 실패!', error)
    })
  }
  
  // 로그인 폼
  const state = reactive({
    username: ref(null)
  })
  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then((response) => {
      console.log('로그인 성공!', response.data.key)
      token.value = response.data.key
      state.username = username
      router.push({ name: 'MainView' })
    })
    .catch((error) => console.log('로그인 실패!', error))
  }
  
  // 로그아웃 폼
  const logOut = function () {
    token.value = null
    router.push({ name: 'MainView' })
    console.log('로그아웃 성공!')
  }
    
  // 스토어 초기화
  const initialize = function () {
    const storedToken = localStorage.getItem('token')
    if (storedToken) {
      token.value = storedToken
    }
  }

  // 메시지 보내기
  const sendMessage = async function (message) {
    messages.value.push({ sender: '나', content: message });

    try {
      const response = await axios.post(
        `${API_URL}/chatbot/chat/`,
        { message },
        { responseType: 'text' }
      );
      const chatbotResponse = response.data;
      messages.value.push({ sender: '챗봇', content: chatbotResponse });
    } catch (error) {
      console.error('There was an error!', error);
      messages.value.push({ sender: 'Error', content: 'Failed to get response from the server.' });
    }
  }

  const isLogin = computed(() => {
    return token.value !== ""
  })
  
  return { 
    state, 
    articles, 
    messages,
    API_URL, 
    getArticles, 
    isLogin, 
    signUp, 
    logIn, 
    logOut, 
    initialize, 
    token,
    sendMessage
  }
}, { persist: true })
