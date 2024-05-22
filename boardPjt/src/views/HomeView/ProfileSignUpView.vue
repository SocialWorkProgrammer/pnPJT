<template>
  <div>
    <h1>가입한 상품 목록</h1>
    <h3>예금</h3>
    <p v-for="deposit in user.sign_up_deposits" :key="deposit.fin_prdt_nm">{{ deposit.fin_prdt_nm }}</p>
    <h3>적금</h3>
    <p v-for="saving in user.sign_up_savings" :key="saving.fin_prdt_nm">{{ saving.fin_prdt_nm }}</p>
    <!-- <div>
      <img :src="histogramSrc" alt="가입한 상품 금리 히스토그램" v-if="histogramSrc">
    </div> -->
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useBoardStore } from '@/stores/counter';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

const route = useRoute();
const store = useBoardStore();
const histogramSrc = ref('')

const user = ref({
  id: null,
  sign_up_deposits: [],
  sign_up_savings: [],
  password: '',
  last_login: '',
  first_name: '',
  last_name: '',
  date_joined: '',
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
});

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/profile/${route.params.username}/detail/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log('프로필 데이터 가져오기 성공!', response);
    user.value = response.data;
  })
  .catch((error) => {
    console.log('프로필을 가져오는 데 있어 오류가 발생했습니다!', error);
  });
});

// 히스토그램을 렌더링하는 함수
onMounted(() => {
  // 다른 프로필 데이터 가져오기
  // ...

  // 히스토그램 이미지 가져오기
  axios.get(`${store.API_URL}/profile/${route.params.username}/detail/histogram`, {
      headers: {
        Authorization: `Token ${store.token}`
      },
      responseType: 'blob' // 이미지를 blob 형식으로 받기 위해 설정
    })
    .then((response) => {
      console.log(response)
      const url = URL.createObjectURL(response.data)
      histogramSrc.value = url
    })
    .catch((error) => {
      console.log('히스토그램 데이터를 가져오는 데 있어 오류가 발생했습니다!', error)
    })
})


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
