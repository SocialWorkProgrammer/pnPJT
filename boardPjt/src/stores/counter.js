import { ref, computed, reactive } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'

export const useBoardStore = defineStore('board', () => {
  const articles = ref([])
  // 로컬 스토리지에 들어갈 때는 모두 문자열로 들어가기 때문에 null 값이 들어가도 ""로 저장하게 된다.
  // 문제는 Vue3를 끄고 켤 때 token을 ref(null)로 하게되면 로컬 스토리지에 token이 아예 안 뜨기 때문에 const token=ref("")으로 하는 것이 낫다.
  const token = ref("")
  const API_URL = "http://127.0.0.1:8000"
  const router = useRouter()
  const route = useRoute()

  

  // 빈 문자열이 아니다 -> 
  
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
  const isLogin = computed(() => {
    return token.value !== ""
  })
  
  return { state, articles, API_URL, getArticles, isLogin, signUp, logIn, logOut, initialize, token }
}, { persist: true })
