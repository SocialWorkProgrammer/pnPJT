<template>
  <div class="container my-container">
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
          <img src="@/assets/커뮤니티.png" class="img-fluid my-image" alt="커뮤니티">
          <div class="label">커뮤니티</div>
        </router-link>
      </div>
      <div class="col-4 d-flex justify-content-center align-items-center">
        <router-link to="/community" class="text-center image">
          <img src="@/assets/커뮤니티.png" class="img-fluid my-image" alt="커뮤니티">
          <div class="label">커뮤니티</div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.my-container {
  max-width: 1200px;
  margin: auto;
}
.image {
  margin : 1rem;
  padding: 1rem;
  border: 1px solid green;
}

.my-image {
  width: 100%;
  height: auto;
  max-width: 200px; /* 이미지 최대 크기 설정 */
}

.label {
  font-size: 1.5rem; /* 텍스트 크기 증가 */
  margin-top: 10px;
  color: #333;
}

@media (min-width: 768px) {
  .my-container {
    padding: 20px;
  }}


</style>