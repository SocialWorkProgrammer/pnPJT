<template>
    <div class="wrapper">
      <div class="boardcontent">
        <h1>금융상품과 관련된 대화를 나누는 게시판입니다.</h1>
        <ArticleList />
        <v-btn
          :to="{ name: 'CreateArticleView' }"
          class="custom-btn"
          color="blue"
        >글 작성</v-btn>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import { useBoardStore } from '@/stores/counter'
  import ArticleList from '@/components/articles/ArticleList.vue'
  const store = useBoardStore()
  
  onMounted(() => {
    store.getArticles()
  })
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
  
  .wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f7f9fc;
    min-height: 100vh;
    font-family: 'Roboto', sans-serif;
  }
  
  .boardcontent {
    padding: 3rem;
    margin: 3rem;
    border-radius: 15px;
    background-color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: left;
    width: 100%; /* 전체 너비 설정 */
    max-width: 1200px; /* 최대 너비 설정 */
  }
  
  h1 {
    margin-bottom: 1.5rem;
    font-size: 2rem;
    color: #333333;
  }
  
  .custom-btn {
    display: static;
    float: inline-end;
    padding: 0.75rem 1.5rem;
    background-color: #0066cc;
    color: #ffffff;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s, box-shadow 0.3s;
    margin-bottom: 2rem; /* 버튼 아래 여백 추가 */
    margin-right: 1rem;
  }
  
  .custom-btn:hover {
    background-color: #004999;
    box-shadow: 0 4px 8px rgba(0, 102, 204, 0.3);
  }
  </style>
  