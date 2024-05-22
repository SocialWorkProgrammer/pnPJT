<template>
  <div class="container">
    <h1 class="title">세레브한 금융상품 추천 리스트</h1>
    <p class="description">
      최신 AI 기술을 적용한 금융상품 추천 리스트입니다.
      <br>가입자는 희망 예치 기간만 입력하면, 서버 측에서 연산을 통해
      만명이 선택한 금융상품들을 분석하고, 걸맞는 세레브한 금융상품을 추천해줍니다.
    </p>

    <div class="recommended-list">
      <div v-for="list in recommended_list" class="category">
        <ul class="product-list">
          <li v-for="deposit in list" :key="deposit.fin_prdt_nm">{{ deposit.fin_prdt_nm }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useBoardStore } from '@/stores/counter'

const store = useBoardStore()
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
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.title {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 20px;
}

.description {
  font-size: 1.1rem;
  color: #666;
  margin-bottom: 30px;
}

.recommended-list {
  margin-top: 20px;
}

.category {
  margin-bottom: 30px;
}

.category h2 {
  font-size: 1.8rem;
  color: #007bff;
  margin-bottom: 10px;
}

.product-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.product-list li {
  font-size: 1.4rem;
  color: #444;
  margin-bottom: 5px;
}
</style>
