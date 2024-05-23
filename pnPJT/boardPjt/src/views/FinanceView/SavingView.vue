<!-- src/components/DepositProducts.vue -->
<template>
  <div class="container">
    <h1><router-link :to="{name: 'DepositView'}">정기예금</router-link> | 정기적금</h1>
    <div class="search-container">
    <label for="bank">은행을 선택하세요:</label>
    <select v-model="selectedBank" id="bank" class="custom-select">
      <option value="">전체은행</option>
      <option v-for="bank in bankList" :key="bank" :value="bank">{{ bank }}</option>
    </select>
    
    <label for="period">예치기간:</label>
    <select v-model="selectedPeriod" id="period" class="custom-select">
      <option value="">전체기간</option>
      <option v-for="period in periodList" :key="period" :value="period">{{ period }}개월</option>
      </select>
    </div>
    <table>
      <thead>
        <tr>
          <th>금융회사명</th>
          <th>상품명</th>
          <th>6개월</th>
          <th>12개월</th>
          <th>24개월</th>
          <th>36개월</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in filteredProducts" :key="product.saving_code">
          <td><RouterLink
          :to="{ name: 'SavingDetailView', params: {id: product.saving_code}}" class="custom-link">{{ product.kor_co_nm }}</RouterLink></td>
          <td><RouterLink
          :to="{ name: 'SavingDetailView', params: {id: product.saving_code}}" class="custom-link">{{ product.fin_prdt_nm }}</RouterLink></td>
          <td>{{ getInterestRate(product, 6) }}</td>
          <td>{{ getInterestRate(product, 12) }}</td>
          <td>{{ getInterestRate(product, 24) }}</td>
          <td>{{ getInterestRate(product, 36) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      savingProducts: [],
      selectedBank: '',
      selectedPeriod: '',
      bankList: [
        '국민은행', '신한은행', '우리은행', '하나은행', '농협은행', 
        '기업은행', '산업은행', '수협은행', '카카오뱅크', '케이뱅크'
      ],
      periodList: [6, 12, 24, 36]
    }
  },
  computed: {
    filteredProducts() {
      return this.savingProducts.filter(product => {
        const matchesBank = this.selectedBank ? product.kor_co_nm.includes(this.selectedBank) : true
        const matchesPeriod = this.selectedPeriod ? product.options.some(option => option.save_trm == this.selectedPeriod) : true
        return matchesBank && matchesPeriod
      })
    }
  },
  mounted() {
    this.fetchSavingProducts()
  },
  methods: {
    async fetchSavingProducts() {
      try {
        const response = await axios.get('http://localhost:8000/finance/saving')
        this.savingProducts = response.data
      } catch (error) {
        console.error('데이터를 가져오는 데 실패했습니다.')
      }
    },
    getInterestRate(product, period) {
      const option = product.options.find(option => option.save_trm == period)
      return option ? option.intr_rate : '-'
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 1000px;
  margin: auto;
  padding: 20px;
}

.search-container {
  margin-bottom: 20px;
}

.search-container label,
.search-container select,
.search-container button {
  margin-right: 10px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

th {
  background-color: #f4f4f4;
}

.custom-link {
  color: inherit; /* 기본 텍스트 색상을 사용 */
  text-decoration: none; /* 밑줄 제거 */
  display: block;

  &:hover {
    color: inherit; /* 마우스를 올렸을 때도 기본 텍스트 색상을 사용 */
    text-decoration: none; /* 마우스를 올렸을 때도 밑줄 제거 */
  }
}

.search-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
<<<<<<< HEAD
  max-width: 400px;
=======
>>>>>>> minho
  margin: auto;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
}

label {
  font-weight: bold;
  color: #333;
}

.custom-select {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  background: white;
  transition: border-color 0.2s ease-in-out;
}

.custom-select:focus {
  border-color: #2980b9;
  outline: none;
}

@media (max-width: 600px) {
  .search-container {
    padding: 15px;
  }

  .custom-select {
    font-size: 14px;
  }
}


</style>
