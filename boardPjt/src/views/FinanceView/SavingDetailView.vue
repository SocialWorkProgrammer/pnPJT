<template>
  <div class="container">
    <div v-if="product" class="product-card">
      <h3>{{ product.fin_prdt_nm }}</h3>
      <p><strong>금융 회사명:</strong> {{ product.kor_co_nm }}</p>
      <p><strong>가입 방법:</strong> {{ product.join_way }}</p>
      <p><strong>만기 후 이자:</strong> {{ product.mtrt_int }}</p>
      <p><strong>우대 조건:</strong> {{ product.spcl_cnd }}</p>
      <p><strong>가입 제한:</strong> {{ product.join_deny }}</p>
      <p><strong>가입 대상:</strong> {{ product.join_member }}</p>
      <p><strong>기타 유의사항:</strong> {{ product.etc_note }}</p>
      <p><strong>최고 한도:</strong> {{ product.max_limit }}</p>
      <button class="join-button" @click="joinProduct">이 상품 가입하기</button>
    </div>
    <div v-else class="loading">
      Loading...
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useBoardStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useBoardStore()
const route = useRoute()
const product = ref(null)


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/finance/saving/${route.params.id}/`
  })
  .then((response) => {
    product.value = response.data
  })
  .catch((error) => {
    console.log('예금 상품을 못 가져옴ㅠㅠ', error)
  })
})

// 상품 가입 로직
const joinProduct = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/finance/saving/signup_saving/${route.params.id}/`,
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
  .then((response) => {
    console.log('상품 추가됨!')
  })
  .catch((error) => {
    console.log('상품 추가 안됨ㅠㅠ')
  })
}

</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  color: #333;
}

.product-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.product-card:hover {
  transform: scale(1.02);
}

h3 {
  color: #2c3e50;
  margin-bottom: 20px;
}

p {
  margin: 10px 0;
}

strong {
  color: #2980b9;
}

.loading {
  text-align: center;
  font-size: 1.5em;
  color: #999;
}

.join-button {
  display: block;
  width: 100%;
  padding: 10px 20px;
  margin-top: 20px;
  background-color: #2980b9;
  color: white;
  font-size: 1.2em;
  font-weight: bold;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.join-button:hover {
  background-color: #3498db;
  transform: scale(1.05);
}

@media (max-width: 600px) {
  .container {
    padding: 10px;
  }

  .product-card {
    padding: 15px;
  }

  h3 {
    font-size: 1.5em;
  }

  p {
    font-size: 1em;
  }

  .join-button {
    font-size: 1em;
  }
}
</style>
