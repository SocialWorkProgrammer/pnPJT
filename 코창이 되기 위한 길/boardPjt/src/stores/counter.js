import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useBoardStore = defineStore('board', () => {
  const articles = ref([])
  const API_URL = "http://70.12.102.167:5173"
  
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      console.log('왜성공?', response)
      articles.value = response.data
    })
    .catch((error) => console.log('하...'), error)
  }


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
      console.log('에러다!', error)
    })
  }

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
      console.log('리스폰스 받았다', response.data.key)
      token.value = response.data.key
      router.push({name: 'home'})
    })
    .catch((error) => console.log('새끼... 기열!', error))

  }


  return { articles, API_URL, getArticles, isLogin, signUp, logIn, router, token }
}, {persist: true})
