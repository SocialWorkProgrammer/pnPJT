<template>
  <div>
    <div class="container">
      <h1 class="section-title">가입한 상품 목록</h1>
      <h3 class="sub-title">예금</h3>
      <p v-for="deposit in user.sign_up_deposits" :key="deposit.fin_prdt_nm" class="item-text">{{ deposit.fin_prdt_nm }}</p>
      <h3 class="sub-title">적금</h3>
      <p v-for="saving in user.sign_up_savings" :key="saving.fin_prdt_nm" class="item-text">{{ saving.fin_prdt_nm }}</p>
    </div>

    <div class="container">
      <h1 class="title">세레브한 금융상품 추천 리스트</h1>
      <p class="description">
        최신 AI 기술을 적용한 금융상품 추천 리스트입니다.
        <br>가입자는 희망 예치 기간만 입력하면, 서버 측에서 연산을 통해
        만명이 선택한 금융상품들을 분석하고, 걸맞는 금융상품을 추천해주고 싶다.
      </p>

      <div class="recommended-list">
        <div v-for="list in recommended_list" class="category">
          <ul class="product-list">
            <li v-for="deposit in list" :key="deposit.fin_prdt_nm" class="product-item">{{ deposit.fin_prdt_nm }}</li>
          </ul>
        </div>
      </div>
    </div>
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

const recommended_list = ref([])

onMounted(() => {
  axios.get(`${store.API_URL}/finance/recommend/product_recommend_period/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((response) => {
      console.log('추천 리스트 데이터 가져오기 성공!', response)
      recommended_list.value = response.data
    })
    .catch((error) => {
      console.log('추천 리스트 데이터를 가져오는 데 있어 오류가 발생했습니다!', error)
    })
})

</script>

<style scoped>
.container {
  max-width: 900px;
  background-color: #f9f9f9;
  border-radius: 10px;
  padding: 30px;
  margin: 20px auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.section-title, .title {
  font-size: 2.5rem;
  color: #333;
  text-align: center;
  margin-bottom: 20px;
}

.sub-title {
  font-size: 2rem;
  color: #333;
  margin-top: 20px;
  margin-bottom: 10px;
}

.item-text {
  font-size: 1.6rem;
  color: #555;
  margin-bottom: 5px;
}

.description {
  font-size: 1.25rem;
  color: #666;
  text-align: center;
  margin-bottom: 30px;
}

.recommended-list {
  margin-top: 20px;
}

.category {
  margin-bottom: 30px;
}

.product-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.product-item {
  font-size: 1.6rem;
  color: #444;
  margin-bottom: 10px;
}

.product-item:hover {
  background-color: #e0e0e0;
}
</style>
