<template>
  <div>
    <nav class="navbar">
      <div class="navtext">
        <RouterLink :to="{ name: 'ArticleView' }">[네이버주식갤러리]</RouterLink>
      </div>
      <div class="nav-mag">마음 편히 소통할 수 있는 공간입니다.</div>
      <div class="navtext">
        <RouterLink :to="{ name: 'MapView' }">[지도]</RouterLink>
      </div>
      <div class="nav-mag">지도를 통해 전국의 은행을 검색할 수 있습니다.</div>
        <RouterLink :to="{ name: 'ExchangeView' }">[환율]</RouterLink>
    </nav>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/counter'
const store = useBoardStore()
onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;700&display=swap');

.navbar {
  background-color: #f0f8ff; /* 밝은 파스텔 블루 */
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  font-family: 'Poppins', sans-serif;
}

.navtext {
  margin: 0 1rem;
  position: relative;
}

.navtext a {
  text-decoration: none;
  color: #333333; /* 진한 회색 */
  font-size: 1.5rem;
  font-weight: 700;
  transition: color 0.3s;
}

.navtext a:hover {
  color: #007acc; /* 선명한 블루 */
}

.nav-mag {
  font-size: 1.25rem;
  padding: 0.5rem 1rem;
  background-color: #ffffff; /* 흰색 */
  border: 1px solid #007acc; /* 선명한 블루 */
  border-radius: 5px;
  color: #333333; /* 진한 회색 */
  display: none;
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  white-space: nowrap;
  transition: opacity 0.3s, visibility 0.3s;
}

.navtext:hover + .nav-mag {
  display: block;
  opacity: 1;
  visibility: visible;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
