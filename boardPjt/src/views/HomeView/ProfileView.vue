<template>
  <div class="container mt-5">
    <div class="card">
      <div class="card-header text-center">
        <h1>{{ user.name }}님의 프로필 페이지</h1>
      </div>
      <div class="card-body">
        <div class="profile-info">
          <p class="profile-item"><span class="item-label">닉네임:</span> {{ user.username }}</p>
          <p class="profile-item"><span class="item-label">이름:</span> {{ user.name }}</p>
          <p class="profile-item"><span class="item-label">이메일:</span> {{ user.email }}</p>
          <p class="profile-item"><span class="item-label">나이:</span> {{ user.age }}</p>
          <p class="profile-item"><span class="item-label">월급:</span> {{ user.salary}}</p>
          <p class="profile-item"><span class="item-label">재산:</span> {{ user.money }}</p>
          <RouterLink v-if="user.username === store.state.username" :to="{name: 'ProfileDetailView', params: user.username}">[프로필 수정하러 가기]</RouterLink></div>
        </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { useBoardStore } from '@/stores/counter'

const store = useBoardStore()
const route = useRoute()
const user = ref({
  username : null,
  name : null,
  email : null,
  age : null,
  money : null,
  salary : null,
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/profile/${route.params.username}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log('프로필 데이터 가져오기 성공!', response.data)
    user.value = response.data
  })
  .catch((error) => {
    console.log('프로필을 가져오는 데 있어 오류가 발생했습니다!', error)
  })
})

</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
}

.card {
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.card-header {
  background-color: #f8f9fa;
  border-bottom: none;
  padding: 1.5rem 1rem;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.card-body {
  padding: 2rem;
}

.profile-info {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 10px;
}

.profile-item {
  margin: 0;
  font-size: 16px;
}

.item-label {
  font-weight: bold;
  margin-right: 5px;
}
</style>
