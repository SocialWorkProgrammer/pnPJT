<template>
  <div>
    <h1>프로필</h1>
    <p>{{ user }}</p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useBoardStore } from '@/stores/counter'

const route = useRoute()
const store = useBoardStore()

// 질문 : Authorization 말고도 다른 것들도 필요한가??(ID, PW 등)
const user = ref(null)
onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/profile/${route.params.username}/detail/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((response) => {
      console.log('프로필 데이터 가져오기 성공!', response)
      user.value = response.data
    })
    .catch((error) => {
      console.log('프로필을 가져오는 데 있어 오류가 발생했습니다!', error)
    })
  })
</script>

<style scoped>

</style>