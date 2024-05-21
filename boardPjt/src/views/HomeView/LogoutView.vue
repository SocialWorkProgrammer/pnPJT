<template>
    <div>
        <button @click.prevent="logout">[로그아웃]</button>
    </div>
</template>

<script setup>
import axios from 'axios'
import { useBoardStore } from '@/stores/counter'
import router from '@/router';
const store = useBoardStore()

// 로그아웃 요청 보내기
const logout = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((response) => {
        console.log(response.data)
        store.token= ''
        router.push({name : 'MainView'})
      })
      .catch((error) => {
        console.log(error)
      })
  }
</script>

<style scoped>

</style>