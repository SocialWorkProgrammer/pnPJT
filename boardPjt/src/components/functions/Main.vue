<template>
  <div class="container">
    <div class="row gy-4">
      <div class="col-4 d-flex justify-content-center align-items-center">
        <router-link to="/map" class="text-center image">
          <img src="@/assets/지도.avif" class="img-fluid my-image" alt="지도">
          <div class="label">지도</div>
        </router-link>
      </div>
      <div class="col-4 d-flex justify-content-center align-items-center">
        <router-link to="/exchange" class="text-center image">
          <img src="@/assets/환율.png" class="img-fluid my-image" alt="환율">
          <div class="label">환율</div>
        </router-link>
      </div>
      <div class="col-4 d-flex justify-content-center align-items-center">
        <router-link to="/community" class="text-center image">
          <img src="@/assets/커뮤니티.png" class="img-fluid my-image" alt="커뮤니티">
          <div class="label">커뮤니티</div>
        </router-link>
      </div>
      <div class="col-4 d-flex justify-content-center align-items-center">
        <router-link to="/community" class="text-center image">
          <img src="@/assets/금융상품.png" class="img-fluid my-image" alt="커뮤니티">
          <div class="label">금융상품</div>
        </router-link>
      </div>
      <div class="col-4 d-flex justify-content-center align-items-center">
        <router-link to="/community" class="text-center image">
          <img src="@/assets/추천 금융상품.jpg" class="img-fluid my-image" alt="커뮤니티">
          <div class="label">추천 금융상품</div>
        </router-link>
      </div>
    </div>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import Carousel from '@/components/functions/Carousel.vue'

</script>

<style scoped>

.image {
  margin : 1rem;
  padding: 1rem;
  border: 2px solid green;
}

.my-image {
  width: 250px;
  height: 250px;
}

.label {
  font-size: 1.5rem; /* 텍스트 크기 증가 */
  margin-top: 10px;
  color: #333;
}

</style>