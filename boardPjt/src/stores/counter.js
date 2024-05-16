import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useBoardStore = defineStore('board', () => {
  const articles = ref([])
  const API_URL = "http://127.0.0.1:8000"
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  
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
    const { username, password1, password2 } = payload
    axios({
      method : 'post',
      url: `${API_URL}/accounts/signup/`,
      data : {
        username, password1, password2
      }
    })
    .then((response) => {
      console.log('회원가입 성공!')
      const password = password1
      logIn({username, password})
    })
    .catch((error) => {
      console.log('회원가입 실패!', error)
    })
  }

// 로그인 폼
  const router = useRouter()
  const token = ref(null)
  const logIn = function (payload) {
    const {username, password} = payload
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
      router.push({name: 'home'})
    })
    .catch((error) => console.log('로그인 실패!', error))

  }


  return { articles, API_URL, getArticles, isLogin, signUp, logIn, router, token }
}, {persist: true})
