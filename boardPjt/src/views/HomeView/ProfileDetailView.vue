<template>
  <div class="container mt-5">
    <div class="card">
      <div class="card-header text-center">
        <h1>{{ user.name }}님의 프로필 페이지</h1>
      </div>
      <div class="card-body">
        <form @submit.prevent="updateProfile">
          <div class="mb-3">
            <label for="username" class="form-label">사용자 이름</label>
            <p>{{ user.username }}</p>
          </div>
          <div class="mb-3">
            <label for="name" class="form-label">이름</label>
            <p>{{ user.name }}</p>
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" id="email" v-model="user.email" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="age" class="form-label">나이</label>
            <input type="number" id="age" v-model="user.age" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="money" class="form-label">재산</label>
            <input type="number" id="money" v-model="user.money" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="salary" class="form-label">월급</label>
            <input type="number" id="salary" v-model="user.salary" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="salary" class="form-label">희망예치기간(예금)</label>
            <input type="number" id="salary" v-model="user.deposit_period" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="salary" class="form-label">희망예치기간</label>
            <input type="number" id="salary" v-model="user.saving_period" class="form-control" />
          </div>

          <button type="submit" class="btn btn-primary w-100">프로필 업데이트</button>
        </form>
      </div>
    </div>
  </div>
  <div>
    <canvas ref="chartCanvas" width="400" height="200"></canvas>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useBoardStore } from '@/stores/counter'
import ProfileSignUpView from './ProfileSignUpView.vue'
import router from '@/router'

const route = useRoute()
const store = useBoardStore()

const user = ref({
  id: null,
  sign_up_deposits: [],
  sign_up_savings: [],
  password: '',
  last_login: '',
  first_name: '',
  last_name: '',
  date_joined: '',
  deposit_period: '',
  saving_period: '',
  email: '',
  age: null,
  money: null,
  salary: null,
  financial_products: null,
  is_active: true,
  is_staff: false,
  is_superuser: false,
  groups: [],
  user_permissions: []
})

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

const updateProfile = () => {
  axios({
    method: 'put',
    url: `${store.API_URL}/profile/${route.params.username}/detail/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: user.value
  })
  .then((response) => {
    console.log('프로필 업데이트 성공!', response)
    router.push({ name: 'ProfileView', params: { id: route.params.username } })
  })
  .catch((error) => {
    console.log('프로필 업데이트에 오류가 발생했습니다!', error)
  })
}
</script>

<style scoped>
.container {
  max-width: 800px;
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

.form-label {
  font-weight: bold;
}

.btn-primary {
  background-color: #007bff;
  border: none;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  border-radius: 5px;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>
