<template>
    <div class="article">
        <RouterLink
        :to="{ name: 'DetailView', params: {id: article.id}}" class="custom-link">{{article.title}}</RouterLink>
        <!-- <p>{{article}}</p> -->
        <p>{{ article.user.username }}</p>
        <hr>
        <!-- article serializer가 잘 나오는지 확인하는 용도 -->
        <!-- <p>{{ article }}</p> -->
    </div>
</template>

<script setup>
import {RouterLink} from 'vue-router'
defineProps({
    article: Object
})
</script>

<style scoped>
.article {
    padding: 0.5rem;
    margin: 0px 10px;
}

.custom-link {
  color: inherit; /* 기본 텍스트 색상을 사용 */
  text-decoration: none; /* 밑줄 제거 */
  font-size: 20px;

  &:hover {
    color: inherit; /* 마우스를 올렸을 때도 기본 텍스트 색상을 사용 */
    text-decoration: none; /* 마우스를 올렸을 때도 밑줄 제거 */
  }
}

</style>