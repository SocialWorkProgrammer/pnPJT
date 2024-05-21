<!-- src/components/DepositProducts.vue -->
<template>
  <div class="container">
    <h1>예금 상품 리스트</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <ul v-else>
      <li v-for="product in depositProducts" :key="product.deposit_code">
        <h3>{{ product.fin_prdt_nm }}</h3>
        <p><strong>금융 회사명:</strong> {{ product.kor_co_nm }}</p>
        <p><strong>가입 방법:</strong> {{ product.join_way }}</p>
        <p><strong>만기 후 이자:</strong> {{ product.mtrt_int }}</p>
        <p><strong>우대 조건:</strong> {{ product.spcl_cnd }}</p>
        <p><strong>가입 제한:</strong> {{ product.join_deny }}</p>
        <p><strong>가입 대상:</strong> {{ product.join_member }}</p>
        <p><strong>기타 유의사항:</strong> {{ product.etc_note }}</p>
        <p><strong>최고 한도:</strong> {{ product.max_limit }}</p>
        <p>{{ product.options }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      savingProducts: [],
      loading: true,
      error: null
    }
  },
  mounted() {
    this.fetchDepositProducts()
  },
  methods: {
    async fetchDepositProducts() {
      try {
        const response = await axios.get('http://localhost:8000/finance/saving')
        this.savingProducts = response.data
      } catch (error) {
        this.error = '데이터를 가져오는 데 실패했습니다.'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
}

h1 {
  text-align: center;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  border: 1px solid #ccc;
  padding: 20px;
  margin-bottom: 10px;
}

h3 {
  margin-top: 0;
}
</style>
