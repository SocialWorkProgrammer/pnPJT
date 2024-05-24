<template>
  <div>
    <nav class="navbar">
      <div class="navtext">
        <RouterLink :to="{ name: 'MainView' }">메인페이지</RouterLink>
      </div>
      <div class="navtext">
        <RouterLink :to="{ name: 'ArticleView' }">소통공간</RouterLink>
      </div>
      <div class="navtext">
        <RouterLink :to="{ name: 'MapView' }">지도</RouterLink>
      </div>
      <div class="navtext"><RouterLink class="navtext" :to="{ name: 'ExchangeView' }">환율</RouterLink></div>
      <div class="navtext"><RouterLink class="navtext" :to="{ name: 'DepositView' }">금융상품</RouterLink></div>
      <div class="menu-container">
        <div class="hamburger-menu" @click="toggleDropdown">
          <img src="@/assets/hamburger-icon.jpg" alt="Menu" class="hamburger-icon" />
        </div>
        <div v-if="isDropdownVisible" class="dropdown-menu">
          <div v-if="store.isLogin">
            <RouterLink :to="{ name: 'ProfileView', params: { username: store.state.username } }" class="account-item">{{ store.state.username }}</RouterLink>
            <LogoutView class="account-item" />
          </div>
          <div v-else>
            <div><RouterLink :to="{ name: 'SignUpView' }" class="account-item">회원가입</RouterLink></div>
            <div><RouterLink :to="{ name: 'LoginView' }" class="account-item">로그인</RouterLink></div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useBoardStore } from '@/stores/counter'
import LogoutView from '@/views/HomeView/LogoutView.vue'
const store = useBoardStore()

const isDropdownVisible = ref(false)

const toggleDropdown = () => {
  isDropdownVisible.value = !isDropdownVisible.value
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;700&display=swap');

.navbar {
  background-color: #f0f8ff; /* 밝은 파스텔 블루 */
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 1rem; /* 패딩 증가 */
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  font-family: 'Poppins', sans-serif;
  position: relative;
}

.navtext {
  margin: 1rem; /* 마진 증가 */
  position: relative;
}

.navtext a {
  text-decoration: none;
  color: #333333; /* 진한 회색 */
  font-size: 1.5rem; /* 글씨 크기 증가 */
  font-weight: 700;
  transition: color 0.3s;
}
.navtext a:hover {
  color: #007acc; /* 선명한 블루 */
}

.menu-container {
  position: relative;
}

.hamburger-menu {
  cursor: pointer;
}

.hamburger-icon {
  width: 3rem;
  height: 3rem;
}

.dropdown-menu {
  position: absolute;
  top: 3rem;
  right: 0;
  background-color: #fff;
  border-radius: 10px;
  padding: 0.25rem;
  display: flex;
  flex-direction: column;
  z-index: 1000;
}

.account-item {
  font-size: 1.5rem;
  color: #333;
  text-decoration: none;
  transition: color 0.3s;
}

.account-item:hover {
  color: #007acc; /* 어두운 블루 */
}
</style>
